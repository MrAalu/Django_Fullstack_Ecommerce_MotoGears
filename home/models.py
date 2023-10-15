from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/")
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    # Created at is only changed once when model is created for first time.
    created_at = models.DateTimeField(auto_now_add=True)

    # Everytime model is updated this field value will be changed
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Users adding Products to cart creates new instance of this model
class OrderItemModel(models.Model):
    # If user not logged in then 'customer' would be null and device_id would be stored
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total_price(self):
        return self.quantity * self.price


# when user goes to Payment, this instance is created
ORDER_STATUS_CHOICES = [
    ("Processing", "Processing"),
    ("Shipping", "Shipping"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
]


class OrderModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default="Processing"
    )

    # Get total Price , Sale price if exists then use that else original Price
