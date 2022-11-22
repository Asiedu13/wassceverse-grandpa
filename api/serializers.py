from rest_framework.serializers import ModelSerializer
from .models import StudentDetails

class StudentSerializer(ModelSerializer):

    class Meta:
        model = StudentDetails
        fields = "__all__"
        