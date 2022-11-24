from django.contrib import admin
from .models import StudentDetails, RegisteredSchools, RegisteredStudents

# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(RegisteredSchools)
admin.site.register(RegisteredStudents)
