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
        username = email.split('@')[0]
        if password != confirm_password:
            messages.success(request, 'Password and confirm password not match .')
            return render(request, 'pages/register.html')
        User.objects.create_user(username=username,full_name=name, email=email, password=confirm_password)
    return render(request, 'pages/register.html')

# Implement Login from office
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        email = email.lower()
        password = request.POST.get('password')
        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            username = user_obj.first().username
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home_page')
    return render(request, 'pages/login.html')