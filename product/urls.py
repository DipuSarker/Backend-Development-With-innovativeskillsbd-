from django.urls import path, include
from .views import *
from .api import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('api', ProductViewSets, basename='pro_viewset')


urlpatterns = [
    path('product/', include(router.urls)),
    # path('', home_page, name='home_page'),
    path('', product_page, name='product_page'),
    path('Product_list_func/', Product_list_func, name='Product_list_func'),
    # path('api/', product_api, name='product_api'),
    path('rest_api/<int:pk>/', ProductViewSets.as_view(), name='rest_api'),
    # path('gen_api/<int:pk>/', GenericProductViewSets.as_view(), name='gen_api'),
] 