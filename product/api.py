
from django.http import JsonResponse

from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework import viewsets, status, generics
from .serializers import *

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # def update(self, request, pk=None):
    #     prod = self.get_object()
    #     serializer = self.get_serializer(prod, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response({'message': 'error'})

# class ProductViewSets(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
class GenericProductViewSets(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializers = self.get_serializer(queryset, many=True)
        return Response(serializers.data)
    
    def partial_update(self, request, pk=None):
        prod = self.get_object()
        serializer = self.get_serializer(prod, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': 'error'})
    
    
    

@api_view(['GET', 'DELETE','PATCH', 'PUT'])
def Product_list_func(request, pk=None):
    if request.method == 'GET':
        products = Product.objects.all()
        s = ProductSerializer(products, many=True)
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        print('Patch')
        prod = Product.objects.get(id=pk)
        serializers = ProductSerializer(prod, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        print('Put')
        prod = Product.objects.get(id=pk)
        serializers = ProductSerializer(prod, data=request.data, partial=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # if request.method == 'PATCH':
    #     prod = Product.object.get(id=pk)
    #     serializer = ProductSerializer(prod, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response({'message': 'error'})
        
    # if request.method == 'PUT':
    #     prod = Product.object.get(id=pk)
    #     serializer = ProductSerializer(prod, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response({'message': 'error'})



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
        
        