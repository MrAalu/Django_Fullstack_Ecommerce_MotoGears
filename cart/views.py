from django.shortcuts import render, redirect
from django.views import View
from home.models import ProductModel, OrderItemModel, OrderModel
from .api.views import get_customer


# Returns individual carts total price ,images, Cart Summary (Subtotal,total cart items Counter)
def getCartDetails(carts):
    sub_total_price = 0  # Sub total price of all Users Cart (++cart_total_price)
    total_cart_items_counter = len(carts)
    cart_items_with_images_title = []
    for cart in carts:
        cart.calculate_total_price()
        sub_total_price = sub_total_price + cart.cart_total_price
        title = cart.product.title
        image = cart.product.image
        cart_items_with_images_title.append(
            {"cart_item": cart, "image": image, "title": title}
        )

    data = {
        "cart_items": cart_items_with_images_title,
        "total_cart_items_counter": total_cart_items_counter,
        "sub_total_price": sub_total_price,
    }
    return data


class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user
            carts = OrderItemModel.objects.filter(customer=customer)

        # User is not logged in (Guest User)
        else:
            device_id = request.COOKIES.get("device")
            carts = OrderItemModel.objects.filter(device_id=device_id)

        data = getCartDetails(carts)
        return render(request, "cart/cart.html", data)


def delete_cart(request, product_id):
    customer = get_customer(request)
    if request.user.is_authenticated:
        cart_item = OrderItemModel.objects.filter(
            product_id=product_id, customer=customer
        )
    else:
        cart_item = OrderItemModel.objects.filter(
            product_id=product_id, device_id=customer
        )

    cart_item.delete()
    return redirect("cart")
