from rest_framework import serializers
from .models import StudentDetails, RegisteredSchools, RegisteredStudents


class MainSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentDetails
        fields = "__all__"

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisteredSchools
        fields = "__all__"

class RgSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisteredStudents
        fields = "__all__"