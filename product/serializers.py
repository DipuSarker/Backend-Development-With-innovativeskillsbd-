from rest_framework import serializers
from .models import * 


class InventorySerializer(serializers.ModelSerializer):
    # quantity = serializers.CharField(max_length=20)
    class Meta:
        model = Inventory
        exclude = ['id','product']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data['quantity'] = InventorySerializer(instance.inventory).data or None
        except Exception:
            data['quantity'] = None
        return data
