from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'route'),
    path('students/', views.getStudents, name='students'),
    path('students/<str:key>/', views.getStudent, name='student'),
    
]
