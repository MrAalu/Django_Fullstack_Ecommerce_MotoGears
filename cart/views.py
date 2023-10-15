from django.shortcuts import render, redirect
from django.views import View
from home.models import OrderItemModel, ProductModel
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.core.exceptions import ValidationError


class CartView(View):
    def get(self, request):
        return render(request, "cart/cart.html")


# Function to get customer i.e. Logged-in user or Guest user's Device ID
def get_customer(request):
    if request.user.is_authenticated:
        customer = request.user  # Authenticated user
    else:
        customer = request.COOKIES.get("device")  # Guest user's device ID
    return customer


# View for adding items to the cart
def addToCartView(request):
    if request.method == "POST":
        # Get the JSON data from the request body
        post_data = json.loads(request.body.decode("utf-8"))
        # print(post_data)

        # Access the 'product_id' and 'quantity' from the JSON data
        product_id = post_data.get("product_id")
        quantity = post_data.get(
            "quantity", 1
        )  # Default to 1 if 'quantity' is not provided

        product = get_object_or_404(ProductModel, id=product_id)  # fetch product
        # check if product has sale price or original price
        if product.sale_price is None:
            product_price = product.original_price
        else:
            product_price = product.sale_price

        data = get_customer(request)

        if data is None:
            return JsonResponse({"message": "Device ID or user is not available."})

        if request.user.is_authenticated:
            # Check if the cart item already exists for the Logged-in user
            try:
                cart = OrderItemModel.objects.get(customer=data, product=product)
            except OrderItemModel.DoesNotExist:
                cart = None

            if cart is not None:
                # The cart item exists, so update the quantity
                cart.quantity += quantity
                cart.save()
            else:
                # Create a new Cart (OrderItemModel) instance for the Logged-in user
                cart = OrderItemModel(
                    customer=data,
                    product=product,
                    quantity=quantity,
                    price=product_price,
                )
        else:
            # Check if the cart item already exists for the Guest user using device ID
            try:
                cart = OrderItemModel.objects.get(device_id=data, product=product)
            except OrderItemModel.DoesNotExist:
                cart = None

            if cart is not None:
                # The cart item exists, so update the quantity
                cart.quantity = cart.quantity + quantity
                cart.save()
            else:
                # Create a new Cart (OrderItemModel) instance for the Guest user using device ID
                cart = OrderItemModel(
                    device_id=data,
                    product=product,
                    quantity=quantity,
                    price=product_price,
                )

        try:
            cart.full_clean()
        except ValidationError as e:
            pass
        cart.save()

        return JsonResponse(
            {"success": True, "message": "Item added to Cart successfully"}
        )


# When a guest user logs in, update the customer in their cart items
# @login_required
# def merge_guest_cart_with_user_cart(request):
#     guest_customer = GuestCustomer.objects.get(device_id=request.COOKIES.get('device'))
#     user_customer = request.user

#     # Update the customer field in OrderItemModel instances for the user
#     OrderItemModel.objects.filter(customer=guest_customer).update(customer=user_customer)

#     # Delete the guest customer record
#     guest_customer.delete()

#     return HttpResponse('Guest cart merged with user cart')
