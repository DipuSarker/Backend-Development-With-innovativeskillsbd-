from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id","name", "product_code", "discounted_price", "retail_price", "is_avaliable", "image"
    ]
    
    ordering = ["id"] # Ordering by descending order

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Inventory)

