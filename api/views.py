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
            'description': 'Returns an array with all the students'
        },
        {
            'Endpoint': '/students/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single student object'
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
            'description': 'Creates an existing student with data sent in post request'
        },
        {
            'Endpoint': '/students/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting student'
        },
        {
            'Endpoint': '/schools/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array with all the schools'
        },
        {
            'Endpoint': '/schools/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single school object'
        },
        {
            'Endpoint': '/reg-students/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array with all the students'
        },
        {
            'Endpoint': '/reg-students/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single student object'
        },
        {
            'Endpoint': '/reg-students/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Add a student to the list of registered students'
        },
        {
            'Endpoint': '/reg-students/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update the details of a registered student with data sent in post request'
        },
        {
            'Endpoint': '/reg-students/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting student from the array of registered students'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getStudents(request):
    students = StudentDetails.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request, key):
    students = StudentDetails.objects.all(index_number = key)
    serializer = StudentSerializer(students, many=False)
    return Response(serializer.data)