from rest_framework import serializers
from .models import ProductsModel

# Serialize Products API for CRUD calls
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'