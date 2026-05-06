from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('dup_check/', dup_check, name='dup_check')
]
