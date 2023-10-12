from django.contrib import admin
from .models import (
    ProductCategory,
    ProductBrand,
    ProductModel,
    OrderItemModel,
    OrderModel,
)

admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
admin.site.register(ProductModel)
admin.site.register(OrderItemModel)
admin.site.register(OrderModel)
