from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('conversation/', views.conversation, name="conversation"),
    path('congrats/', views.congrats, name="congrats"),
    path('camera/', views.camera, name="camera"),
    path('fingerprint/', views.fingerprint, name='fingerprint'),
]
