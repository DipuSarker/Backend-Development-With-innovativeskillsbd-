from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from user.models import User

class TokenRefreshViewCustomSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        # Get user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")
        
        # Authenticate user with username and password
        authenticated_user = authenticate(username=user.username, password=password)
        
        if authenticated_user is None:
            raise serializers.ValidationError("Invalid email or password")
        
        # Return user in validated_data
        attrs['user'] = authenticated_user
        return attrs