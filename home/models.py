from django.db import models
from django.contrib.auth.models import User


product_category_choices = {
    "Exhauts",
    "Stickers",
    "Helmets",
    "Jackets",
    "Gloves",
    "Masks",
    "Pants",
    "Boots",
}
# Not a VALID Choice


# class ProductModel(models.Model):
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to="products/")
#     original_price = models.DecimalField()
#     sale_price = models.DecimalField()
#     description = models.TextField()
#     category = models.Choices(product_category_choices)
#     brand = models.CharField()
#     quantity = models.IntegerField()
#     created_at = models.DateField(auto_now=True)


# TODO : Category pani afai le create garna milne
# Brand also
