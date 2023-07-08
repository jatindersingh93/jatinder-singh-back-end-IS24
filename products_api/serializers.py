from rest_framework import serializers
from .models import ProductsModel
from utils.models import ProductSizes


# Serialize Products API for CRUD calls
class ProductsSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    class Meta:
        model = ProductsModel
        fields = '__all__'
    
    def get_size(self, instance):        
        return ProductSizes(instance.size).name