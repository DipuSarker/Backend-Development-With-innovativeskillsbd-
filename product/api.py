
from product.models import Product


def product_api(request):
    limit = request.GET.get('limit', 1)
    offset = request.GET.get('offset', 0)
    search = request.GET.get('search')
    
    products = Product.objects.all()