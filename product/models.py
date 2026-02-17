from django.db import models
from django_resized import ResizedImageField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Color(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    product_code = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)
    image = ResizedImageField(size=[500,300], quality=75, upload_to='products_img/', blank=True, null=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_avaliable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.product} - {self.quantity}"
    
 