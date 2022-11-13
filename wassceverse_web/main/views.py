from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import StudentCred

# Create your views here.
def login(request):
    if request.method == "POST":
        form = StudentCred(request.POST)
        if form.is_valid:
            HttpResponseRedirect('conversation')
    else:
        form = StudentCred()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

def conversation(request):
    return render(request, 'conversation.html')

def congrats(request):
    return render(request, 'congrats.html')
