from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page(request):
    return render(request, 'pages/index.html')

# @login_required
def product_page(request):
    products = Product.objects.filter(discounted_price__gt=0)
    context = {'discounted_price': products}
    return render(request, 'pages/index.html', context)