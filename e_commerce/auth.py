from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from user.models import User
from django.contrib import messages
from rest_framework_simplejwt.views import TokenObtainPairView
from e_commerce.auth_serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

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



class TokenRefreshViewCustomView(APIView):
    serializer_class = TokenRefreshViewCustomSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        data = {
            'username': user.username,
            'email': user.email,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        return Response(data)