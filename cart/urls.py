from django.urls import path
from .views import CartView
from .api.views import addToCart, cart_item_counter

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("api/add-to-cart/", addToCart),  # API
    path("api/cart-item-counter/", cart_item_counter),  # API
]
