from rest_framework import serializers
from .models import ProductsModel
from utils.models import ProductSizes


# Serialize Products API for CRUD calls
class ProductsSerializer(serializers.ModelSerializer):
    size_display = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ProductsModel
        fields = '__all__'
    
    # Read only to display enum name
    def get_size_display(self, instance):
        return ProductSizes(instance.size).name