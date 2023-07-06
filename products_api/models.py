import uuid
from django.db import models
from utils.models import ProductSizes

class ProductsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    colour = models.CharField(max_length=100, null=True, blank=True)
    size = models.PositiveSmallIntegerField(
        choices=ProductSizes.choices(), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products"