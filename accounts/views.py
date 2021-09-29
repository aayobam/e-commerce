import email
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages

def user_account(request):
    return HttpResponse("<h1>Welcome to your user account!</h1>")

def user_registration(request):
    return render(request,'accounts/register.html') 


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, username=username,password=password)
        # Verify user is valid
        if user is not None:
            account = Profile.objects.filter(user=user)
            # login(request, account)
            return redirect('user-account')
        else:
            return render(request,'accounts/login.html')
    else:
          return render(request,'accounts/login.html')
