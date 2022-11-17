from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from . import models
from .forms import StudentCred

import base64
import io
from PIL import Image
from autocrop import Cropper
import os
import mariadb

# Create your views here.


def login(request):
    context = {'error': ""}
    if request.method == "POST":
        form = StudentCred(request.POST)
        if form.is_valid:
            state = False
            duplicate = False
            try:
                studentData = models.StudentDetails.objects.get(
                    index_number=request.POST['index_number'])
            except ObjectDoesNotExist:
                state = True

            except MultipleObjectsReturned:
                duplicate = True

            if state:
                context['error'] = "Your index number does not exist on our system.Please contact your school administration"

            elif duplicate:
                context['error'] = "Your index number appears to be duplicate on our system.Please contact your school administration"
            elif studentData.student_key == "":  # type: ignore
                context['error'] = "You do not have a key. Please contact your school administration"
            # type: ignore
            elif studentData.student_key == request.POST['student_key']:
                request.session['student'] = studentData.id  # type: ignore
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

    if request.method == "POST":
        form = StudentCred(request.POST)
        if form.is_valid:
            studentData = models.StudentDetails.objects.get(
                id=request.session['student'])
            studentData.surname = request.POST['surname_final']
            studentData.first_name = request.POST['first_name_final']
            studentData.other_names = request.POST['other_names_final']
            studentData.course = request.POST['course_final']
            studentData.class_field = request.POST['class_final']
            studentData.electives = request.POST['electives_final']
            studentData.date_of_birth = request.POST['date_of_birth_final']
            studentData.parent_contact = request.POST['parent_contact_final']
            if request.POST['gender_final'] == 'male':
                studentData.gender = 0
            elif request.POST['gender_final'] == 'female':
                studentData.gender = 1
            studentData.save()

            try:
                studentReg = models.RegisteredStudents.objects.get(
                    student=request.session['student'])
            except ObjectDoesNotExist:
                record = models.RegisteredStudents(
                    student=request.session['student'])
                record.save()
            print(request.POST['has_camera'])
            if request.POST['has_camera'] == "no":
                return redirect('congrats')
            elif request.POST['has_camera'] == 'yes':
                return redirect('camera')

    student = request.session['student']
    studentData = models.StudentDetails.objects.get(id=student)
    school = studentData.school
    other_names = ""
    if studentData.other_names != "undefined":
        other_names = studentData.other_names
    context = {
        'id': student,
        'school': school,
        'surname': studentData.surname,
        'first_name': studentData.first_name,
        'other_names': other_names,
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


def camera(request):
    context = {}
    if 'student' not in request.session:
        return redirect('login')

    if request.method == "POST":
        url = str.encode(request.POST['blobData'])
        z = url[url.find(b'/9'):]
        im = Image.open(io.BytesIO(base64.b64decode(z)))
        path_url = "main/test.jpg"
        im.save(path_url)
        cropper = Cropper(
            width=150,
            height=200,
            face_percent=40
        )
        cropped_array = cropper.crop(path_url)

        # Save the cropped image with PIL if a face was detected:
        try:
            if len(cropped_array) != 0:
                print("Ok")
                cropped_image = Image.fromarray(cropped_array).open
                cropped_image.save(path_url)

        except TypeError:
            print("Try Again")
            context["error"] = "Try Again"
        
        with open(path_url, 'rb') as input_file:
            ablob = input_file.read()
            
        studentData = models.StudentDetails.objects.get(id=student)
        studentData.image = ablob
        return redirect('congrats')

    return render(request, 'passport_pic.html')


def fingerprint(request):
    return render(request, "fingerprint.html")
