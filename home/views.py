from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import ProductModel, OrderItemModel
from decimal import Decimal
from django.http import JsonResponse


# User is loggedin , merge the guest cart
# When merging if Loggedin user already has same Item in cart then just increment the quantity
def merge_guest_and_user_cart(request):
    # DeviceID match gareko ma for loop layera customer value insert gardine
    device_id = request.COOKIES.get("device")

    # Guest users Cart
    guest_carts = OrderItemModel.objects.filter(device_id=device_id)

    # Authenticated users Cart
    authenticated_user_carts = OrderItemModel.objects.filter(customer=request.user)

    # Storing all Cart items Products ID of Authenticated User
    authenticated_user_cart_productIds = []

    for cart in authenticated_user_carts:
        authenticated_user_cart_productIds.append(cart.product_id)

    # Merge the carts
    for guest_cart in guest_carts:
        if guest_cart.product_id in authenticated_user_cart_productIds:
            # Here, we will update cart in Authenticated Users OrderItemModel and then delete the Respective Guest Cart
            repeated_cart = authenticated_user_carts.get(
                product_id=guest_cart.product_id, customer=request.user
            )
            repeated_cart.quantity += guest_cart.quantity
            repeated_cart.save()
            guest_cart.delete()
        else:
            # Cart is Unique,so changing the Guest cart into Authenticated Users Cart
            guest_cart.customer = request.user
            guest_cart.device_id = None
            guest_cart.save()


class Homepage(View):
    def get(self, request):
        # Fetch only 4 recent updated products with Discounts
        discount_products = ProductModel.objects.filter(
            sale_price__isnull=False
        ).order_by("-updated_at")[:4]

        # Calculate discount percentage for each product
        for product in discount_products:
            discount_percentage = (
                (product.original_price - product.sale_price) / product.original_price
            ) * 100

            # Decimal() to make Precise Decimal Conversion, Quantize() to make decimal places of 2
            product.discount_percentage = Decimal(discount_percentage).quantize(
                Decimal("0.00")
            )

        # recent products (new arrivals) fetching
        new_arrival_products = ProductModel.objects.order_by("-created_at")[:4]

        data = {
            "discount_products": discount_products,
            "new_arrival_products": new_arrival_products,
        }

        if request.user.is_authenticated:
            # User is loggedin , merge the guest cart
            merge_guest_and_user_cart(request)

        return render(request, "home/index.html", data)
