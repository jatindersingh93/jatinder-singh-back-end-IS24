from django.db import models
from utils.models import ProductSizes

# Define Schema to products model
class ProductsModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    colour = models.CharField(max_length=100, null=True, blank=True)
    size = models.PositiveSmallIntegerField(
        choices=ProductSizes.choices(), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products"