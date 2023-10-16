from django.urls import path
from .views import CartView, delete_cart
from .api.views import addToCart, cart_item_counter

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("api/add-to-cart/", addToCart),  # API
    path("api/cart-item-counter/", cart_item_counter),  # API
    path("delete-cart/<int:product_id>/", delete_cart, name="delete-cart"),
]
