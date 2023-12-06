from django.db import models
from django.contrib.auth.models import User


class DeliveryInformationModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # After this object is as 'FK' with OrderModel,we change is_active=True.
    # If we visits the Homepage, we will run a Query where is_activate=False DeliveryModels will be Deleted
    is_active = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f"{self.full_name} - {self.address_line1} , {self.address_line2} , {self.city} - {self.phone_number}"
