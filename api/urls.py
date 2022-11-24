from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('students/', views.getStudents, name="students"),
    path('students/<str:index>/', views.getStudent, name="student"),
]