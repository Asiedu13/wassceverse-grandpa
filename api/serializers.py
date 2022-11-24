from rest_framework.serializers import ModelSerializer
from .models import StudentDetails, RegisteredSchools, RegisteredStudents

class StudentSerializer(ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = "__all__"