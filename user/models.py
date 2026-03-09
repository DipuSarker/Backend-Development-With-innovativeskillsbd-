from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=11)
    
#     def __str__(self):
#         return self.user.username
class User(AbstractUser):
    first_name = None
    last_name = None
    
    full_name = models.CharField(max_length = 255, blank=True, null = True)
    phone = models.CharField(max_length = 11, blank=True, null = True)
    
    
   