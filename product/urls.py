from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # path('', home_page, name='home_page'),
    path('', product_page, name='product_page'),
    path('api/', product_api, name='product_api'),
]
