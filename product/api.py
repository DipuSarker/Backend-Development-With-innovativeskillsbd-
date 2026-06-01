
from django.http import JsonResponse

from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import viewsets, status, generics
from .serializers import *

# class ProductViewSets(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSets(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# class GenericProductViewSets(viewsets.GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializers = self.get_serializer(queryset, many=True)
        return Response(serializers.data)

@api_view(['GET', 'DELETE'])
def Product_list_func(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_404_NOT_FOUND)
    



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
        
        