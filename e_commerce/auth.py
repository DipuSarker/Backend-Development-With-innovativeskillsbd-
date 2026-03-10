from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from user.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name', '')
        email = data.get('email', '')
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')
        
        if password != confirm_password:
            messages.success(request, 'Password and confirm password not match .')
            return render(request, 'pages/register.html')
        User.objects.create(full_name=name, email=email, password=confirm_password)
    return render(request, 'pages/register.html')