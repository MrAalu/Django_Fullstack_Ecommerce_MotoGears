from django.urls import path
from .views import CartView
from .api.views import addToCartView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("api/add-to-cart/", addToCartView),  # API
]
