from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import models
from .forms import StudentCred

# Create your views here.
def login(request):
    context = {'error': ""}
    if request.method == "POST":
        form = StudentCred(request.POST)
        if form.is_valid:
            studentData = models.StudentDetails.objects.get(index_number = request.POST['index_number'])
            if studentData.student_key == "":
                context['error'] = "You do not have a key. Please contact your school administration" 
            elif studentData.student_key == request.POST['student_key']:
                request.session['student'] = studentData.id
                return redirect("conversation")
            else:
                context['error'] = "Your key is incorrect. Please contact your school administration if you have recieved the wrong key"

    else:
        form = StudentCred()
    context['form'] = form  # type: ignore
    return render(request, 'login.html', context)

def conversation(request):
    if 'student' not in request.session:
        print('Hello')
        HttpResponseRedirect('login')
    
    student = request.session['student']
    print(student)
    studentData = models.StudentDetails.objects.get(id = student)
    school = studentData.school
    print(school)
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
