from django.urls import path
from .views import MainListAPIView


urlpatterns = [
    path('main/', MainListAPIView.as_view(), name='main'),
    
]
