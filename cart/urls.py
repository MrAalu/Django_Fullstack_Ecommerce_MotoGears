from django.urls import path
from .views import CartView, addToCartView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add-to-cart/", addToCartView),  # API
]
