from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("authentication was successfull")
            else:
                return HttpResponse("Authentication was failed, try again")


    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def add(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        result = float(num1) + float(num2)
        return render(request, 'add.html', {'result': result})
    return render(request, 'add.html', {})


def subtract(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        result = float(num1) - float(num2)
        return render(request, 'subtract.html', {'result': result})
    return render(request, 'subtract.html', {})


def multi(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        result = float(num1) * float(num2)
        return render(request, 'multi.html', {'result': result})
    return render(request, 'multi.html', {})


def divide(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        result = float(num1) / float(num2)
        return render(request, 'divide.html', {'result': result})
    return render(request, 'divide.html', {})
