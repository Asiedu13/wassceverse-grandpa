from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import StudentDetails
from .serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/students/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of all students'
        },
        {
            'Endpoint': '/students/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single student_details object'
        },
        {
            'Endpoint': '/students/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new student with data sent in post request'
        },
        {
            'Endpoint': '/students/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Modifies an existing student with data sent in post request'
        },
        {
            'Endpoint': '/students/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing student'
        },
        {
            'Endpoint': '/schools/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of all schools'
        },
        {
            'Endpoint': '/schools/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single school object'
        },
        {
            'Endpoint': '/rg_students/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of all registsered_students'
        },
        {
            'Endpoint': '/rg_students/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single registered_student object'
        },
        {
            'Endpoint': '/rg_students/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Add a student to the registered list with data sent in post request'
        },
        {
            'Endpoint': '/rg_students/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Modifies an existing registered student with data sent in post request'
        },
        {
            'Endpoint': '/rg_students/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing student from the registered list'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getStudents(request):
    students = StudentDetails.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request, index):
    students = StudentDetails.objects.get(index_number=index)
    serializer = StudentSerializer(students, many = False)
    return Response(serializer.data)
