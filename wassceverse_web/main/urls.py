from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('_/', views.conversation, name="conversation"),
    path('*/', views.congrats, name="congrats")
]
