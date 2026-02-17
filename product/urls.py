from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('product/', product_page, name='product_page'),
]
