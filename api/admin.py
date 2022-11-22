from django.contrib import admin

# Register your models here.
from .models import StudentDetails, RegisteredSchools

admin.site.register(StudentDetails)
admin.site.register(RegisteredSchools)