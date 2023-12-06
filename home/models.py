from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid
from checkout.models import DeliveryInformationModel


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
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="products"
    )
    brand = models.ForeignKey(
        ProductBrand, on_delete=models.CASCADE, related_name="products"
    )
    quantity = models.PositiveIntegerField()

    # Created at is only changed once when model is created for first time.
    created_at = models.DateTimeField(auto_now_add=True)

    # Everytime model is updated this field value will be changed
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# (CART Model) Users adding Products to cart creates new instance of this model
class OrderItemModel(models.Model):
    # If user not logged in then 'customer' would be null and device_id would be stored
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cart_total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def __init__(self, *args, **kwargs):
        super(OrderItemModel, self).__init__(*args, **kwargs)
        # Calculate total price when the instance is created
        self.cart_total_price = self.quantity * self.price

    def save(self, *args, **kwargs):
        # Recalculate total price before saving updates
        self.cart_total_price = self.quantity * self.price
        super(OrderItemModel, self).save(*args, **kwargs)


ORDER_STATUS_CHOICES = [
    ("Processing", "Processing"),
    ("Shipping", "Shipping"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
]


# when user places the Order,this model object is Created
class OrderModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_information = models.ForeignKey(
        DeliveryInformationModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default="Processing"
    )
    payment_type = models.CharField(max_length=50, editable=False)
    track_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # This becomes 'True' Only after the Webhook returns payment_intent.success or admin updates it on AdminPanel
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - Order Track ID : {self.track_id} | Payment Type : {self.payment_type} , Paid : {self.is_paid} | Order Status : {self.order_status}"


# After OrderModel is created,this object is created to represent which items,qty. was Purchased by User
class PurchasedItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cart_total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
