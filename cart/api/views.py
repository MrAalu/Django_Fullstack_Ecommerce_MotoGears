from home.models import OrderItemModel, ProductModel
from django.shortcuts import get_object_or_404
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Function to get customer i.e. Logged-in user or Guest user's Device ID
def get_customer(request):
    if request.user.is_authenticated:
        customer = request.user  # Authenticated user
    else:
        customer = request.COOKIES.get("device")  # Guest user's device ID
    return customer


# View for adding items to the cart
@api_view(["POST"])
def addToCart(request):
    # Get the JSON data from the request body
    post_data = request.data
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
        return Response(
            {
                "success": False,
                "message": "Failed to add item to Cart",
                "details": "Device ID or user is not available.",
            }
        )

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
    # User is not loggedin
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

    cart.save()
    return Response({"success": True, "message": "Successfully added item to Cart"})


# Fetch Cart Item Counter for NAVBAR
@api_view(["GET"])
def cart_item_counter(request):
    if request.user.is_authenticated:
        carts = OrderItemModel.objects.filter(customer=request.user)
    else:
        device_id = request.COOKIES.get("device")
        carts = OrderItemModel.objects.filter(device_id=device_id)
    total_carts = len(carts)
    return Response(
        {
            "success": True,
            "total_carts": total_carts,
            "message": "Cart Item Counter Fetched Successfully",
        }
    )
