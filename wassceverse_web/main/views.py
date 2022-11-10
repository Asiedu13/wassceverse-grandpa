from django.shortcuts import render
from . import models

# Create your views here.
def login(request):
    schools = models.RegisteredSchools.objects.all().values()
    context = {
        "schools": schools,
    }
    return render(request, 'login.html', context)

def conversation(request):
    return render(request, 'conversation.html')

def congrats(request):
    return render(request, 'congrats.html')
