# API To Update Cart Quantity from Cart.html page

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import get_customer
from home.models import OrderItemModel


# Return Total_Qty, Cart Total , Grand Total of ALL Cart Items
@api_view(["POST"])
def updateCartQuantity(request):
    post_data = request.data
    product_id = post_data.get("product_id")
    new_quantity = post_data.get("new_Quantity")

    customer = get_customer(request)

    if request.user.is_authenticated:
        carts = OrderItemModel.objects.get(customer=customer, product_id=product_id)
    else:
        carts = OrderItemModel.objects.get(device_id=customer, product_id=product_id)

    carts.quantity = new_quantity
    carts.save()
    subtotal = carts.cart_total_price

    if request.user.is_authenticated:
        all_carts = OrderItemModel.objects.filter(customer=customer)
    else:
        all_carts = OrderItemModel.objects.filter(device_id=customer)

    grand_total = 0  # Sub total price of all Users Cart (++cart_total_price)

    for i in all_carts:
        grand_total = grand_total + i.cart_total_price

    return Response(
        {
            "success": True,
            "new_quantity": new_quantity,
            "sub_total": subtotal,
            "grand_total": grand_total,
        }
    )
