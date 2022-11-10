from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def conversation(request):
    return render(request, 'conversation.html')

def congrats(request):
    return render(request, 'congrats.html')
