from django.urls import path
from .views import ViewProduct

urlpatterns = [
    path("product/<int:product_id>/", ViewProduct.as_view(), name="view_product")
]
