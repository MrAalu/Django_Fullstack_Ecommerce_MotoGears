from django.urls import path
from .views import ViewProduct, Shop

urlpatterns = [
    path("", Shop.as_view(), name="shop"),
    path("product/<int:product_id>/", ViewProduct.as_view(), name="view_product"),
]
