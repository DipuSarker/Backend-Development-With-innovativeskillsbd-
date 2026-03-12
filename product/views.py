from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page(request):
    return render(request, 'pages/home.html')

@login_required
def product_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pages/product.html', context)