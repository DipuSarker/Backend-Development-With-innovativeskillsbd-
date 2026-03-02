from django.shortcuts import render
from .models import *
# Create your views here.


def home_page(request):
    return render(request, 'pages/home.html')

def product_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pages/product.html', context)