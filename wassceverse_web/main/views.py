from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist

from . import models
from .forms import StudentCred


# Create your views here.
def login(request):
    context = {'error': ""}
    if request.method == "POST":
        form = StudentCred(request.POST)
        if form.is_valid:
            print("hello")
            state = False
            try:
                studentData = models.StudentDetails.objects.get(index_number = request.POST['index_number'])
            except ObjectDoesNotExist:
                state = True
            if state:
                context['error'] = "Your index number does not exist on our system.Please contact your school administration"
            elif studentData.student_key == "": # type: ignore
                context['error'] = "You do not have a key. Please contact your school administration" 
            elif studentData.student_key == request.POST['student_key']: # type: ignore
                request.session['student'] = studentData.id # type: ignore
                return redirect("conversation")
            else:
                context['error'] = "Your key is incorrect. Please contact your school administration if you have recieved the wrong key"

    else:
        form = StudentCred()
    context['form'] = form  # type: ignore
    return render(request, 'login.html', context)

def conversation(request):
    if 'student' not in request.session:
        return redirect('login')
    
    student = request.session['student']
    studentData = models.StudentDetails.objects.get(id = student)
    school = studentData.school
    context = {
        'id': student,
        'school': school,
        'surname': studentData.surname,
        'first_name': studentData.first_name,
        'other_names': studentData.other_names,
        'course': studentData.course,
        'class': studentData.class_field,
        'index_number': studentData.index_number,
        'electives': studentData.electives,
        'gender': studentData.gender,
        'parent_contact': studentData.parent_contact,
        'dob': studentData.date_of_birth,
    }
    return render(request, 'conversation.html', context)

def congrats(request):
    return render(request, 'congrats.html')
