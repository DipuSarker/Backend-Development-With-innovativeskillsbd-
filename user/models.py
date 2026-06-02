from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=11)
    
#     def __str__(self):
#         return self.user.username

# Role_data = [
#     ('admin', 'Admin'),
#     ('customer', 'Customer')
# ]
class User(AbstractUser):
    first_name = None
    last_name = None
    
    full_name = models.CharField(max_length = 255, blank=True, null = True)
    phone = models.CharField(max_length = 11, blank=True, null = True)
    class RoleData(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CUSTOMER = 'customer', 'Customer'
        MANAGER = 'manager', 'Manager'
    # role = models.CharField(max_length=100, blank=True, null=True, choices=Role_data)
    role = models.CharField(max_length=100, choices=RoleData.choices, default=RoleData.ADMIN)
    
    
    
   