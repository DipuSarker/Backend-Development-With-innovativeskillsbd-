
from django.http import JsonResponse

from product.models import Product


def product_api(request):
    limit = request.GET.get('limit', 1)
    offset = request.GET.get('offset', 0)
    search = request.GET.get('search')
    
    products = Product.objects.all()
    
    if search:
        products = products.objects.filter(name__icontains = search)
        
    start = offset
    end = offset+limit
    new_data = products[start:end]
    
    products = list(new_data.values('name'))
    
    return JsonResponse({
        'data': products
    })
        
        