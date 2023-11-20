from django.urls import path
from .views import (
    CheckoutView,
    successView,
    successCashOnDeliveryView,
    cancelView,
    my_webhook_view,
)
from .api.handleShippingDetails import handleShippingForm

urlpatterns = [
    path("", CheckoutView.as_view(), name="checkout"),
    path("api/handle-shipping-form/", handleShippingForm),  # API
    path("success-cod/", successCashOnDeliveryView, name="success-cod"),
    path("success/", successView, name="success"),
    path("cancelled/", cancelView, name="cancelled"),
    # Very Imp : Dont use the Trailing Slash
    path("webhook/stripe", my_webhook_view, name="webhook-stripe"),
]
