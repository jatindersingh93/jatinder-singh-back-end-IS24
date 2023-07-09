from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets
from .serializers import ProductsSerializer
from .models import ProductsModel
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import serializers
from rest_framework_swagger.views import get_swagger_view
from datetime import datetime
import json
from rest_framework.views import APIView

# Main Class to handle Products API CRUD calls
class ProductsView(APIView):
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    # @product_list will handle GET and POST calls
    @api_view(['GET', 'POST'])
    def products_list(request):        
        if request.method == 'GET':        
            try: 
                products = ProductsModel.objects.all()
                
                title = request.GET.get('name', None)
                if title is not None:
                    products = products.filter(title__icontains=title)
                
                products_serializer = ProductsSerializer(products, many=True)
                return JsonResponse(products_serializer.data, safe=False)
            except Exception as e:
                return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'POST':  
            try:
                product_serializer = ProductsSerializer(data=request.data)
                if product_serializer.is_valid():
                    product_serializer.save()
                    return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except  Exception as e:
                return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST, safe=False)        
    
    # @product_detail Rest View to handle PUT, PATCH and DELETE calls
    @api_view(['GET', 'PUT', 'PATCH','DELETE'])
    def product_detail(request, pk):              
        try: 
            product = ProductsModel.objects.get(pk=pk)
            if request.method == 'GET':             
                product_serializer = ProductsSerializer(product) 
                return JsonResponse(product_serializer.data) 
            elif request.method == 'DELETE': 
                    product.delete() 
                    return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        
            elif request.method == 'PUT':             
                    product_data = JSONParser().parse(request)         
                    product_serializer = ProductsSerializer(data=product_data)
                    if product_serializer.is_valid():
                        instance = product_serializer.update(product, product_data)
                        return JsonResponse(product_data, status=status.HTTP_201_CREATED, safe=False) 
                    return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
        except Exception as e:
            return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST) 