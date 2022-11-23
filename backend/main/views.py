from django.shortcuts import render
from rest_framework import generics
from .models import StudentDetails
from .serializers import MainSerializer, RgSerializer, SchoolSerializer


# Create your views here.
class MainListAPIView(generics.ListAPIView):
    serializer_class = MainSerializer()

    def get_queryset(self):
        return StudentDetails.objects.all()
    
