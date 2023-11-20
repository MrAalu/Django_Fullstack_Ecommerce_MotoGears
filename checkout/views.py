from django.shortcuts import render, redirect
from django.views import View
from home.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import DeliveryForm
from django.db import transaction
from .models import DeliveryInformationModel


import stripe
from django.conf import settings
from django.urls import reverse


# STRIPE Server Side Event Handler for Webhook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# This is the test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET


"""
Payment/Checkout LOGIC :

After user fills the Shipping Form & Submits the Payment type :
-We will create the OrderModel with is_paid=False 
-Then, we create PurchasedItemModel with all the items user purchased i.e.Copy paste Cart to PurchasedItemModel 
-Then, we clear the Old Carts

After that,
if Payment type == Cash-On-Delivery 
-Then,After the Delivery Boi receives the Money,admin can Update the OrderModel is_paid=True & order_status = "Delivered"
-Then, we decrement Product stock quantity manually

if Payment type == Stripe || Debit-Card
-Then,After the Webhook for checkout.session.completed=True is received then fulfill_order() function is invoked.
-In this function,we will update the OrderModel is_paid=True  and Decrement products Quantity

After all this , if user again goes back to shopping and starts adding the items to cart and goes to checkout page
-Then, again user will have to Fill the Shipping Form (User can have Multiple Shipping Detail for each individual OrderModel)
-Then , this whole process will Repeat
"""


# renders Checkout.html and passes users Cart items i.e. 'Your Orders'
@method_decorator(login_required(login_url="/accounts/login/"), name="dispatch")
class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        ordered_items = OrderItemModel.objects.filter(customer=request.user)

        grand_total = 0
        for i in ordered_items:
            grand_total = i.cart_total_price + grand_total

        delivery_form = DeliveryForm()

        data = {
            "ordered_items": ordered_items,
            "grand_total": grand_total,
            "delivery_form": delivery_form,
        }
        return render(request, "checkout/checkout.html", data)

    def post(self, *args, **kwargs):
        host = self.request.get_host()

        # Get users Cart total Price (Ordered Items Grand Total)
        cart_items = OrderItemModel.objects.filter(customer=self.request.user)

        grand_total_price = 0
        for cart in cart_items:
            grand_total_price = grand_total_price + cart.cart_total_price

        latest_delivery_information = (
            DeliveryInformationModel.objects.filter(customer=self.request.user)
            .order_by("-created_at")
            .first()
        )
        latest_delivery_information.is_active = True
        latest_delivery_information.save()

        # Creates order and copies Current Cart items to Purchased Items and Deleting old Carts
        def create_order(payment_type):
            order = OrderModel.objects.create(
                customer=self.request.user,
                delivery_information=latest_delivery_information,
                total_amount=grand_total_price,
                payment_type=payment_type,
            )

            purchased_items = []
            with transaction.atomic():
                for cart_item in cart_items:
                    purchased_item = PurchasedItemModel(
                        order=order,
                        product=cart_item.product,
                        quantity=cart_item.quantity,
                        price=cart_item.price,
                        cart_total_price=cart_item.cart_total_price,
                    )
                    purchased_items.append(purchased_item)
                purchased_items = PurchasedItemModel.objects.bulk_create(
                    purchased_items
                )

            # Delete Old Carts
            for cart in cart_items:
                cart.delete()

            # this is used for line_items
            data = {"order": order, "purchased_items": purchased_items}
            return data

        # Fetch the selected payment type from the form data i.e. 'Debit-Card' || 'Cash-On-Delivery'
        payment_type = self.request.POST.get("payment-type")

        if payment_type == "Debit-Card":
            data = create_order("Debit-Card")
            order = data["order"]
            purchased_items = data["purchased_items"]

            # Creating a list of line items for the Checkout Session
            line_items = []

            for purchased_item in purchased_items:
                line_item = {
                    "price_data": {
                        "currency": "npr",
                        "unit_amount": int(purchased_item.price * 100),
                        "product_data": {
                            "name": purchased_item.product,
                            # Once the Project is Deployed we can use Images
                            "images": [
                                "https://cpmr-islands.org/wp-content/uploads/sites/4/2019/07/Test-Logo-Small-Black-transparent-1.png"
                            ],
                        },
                    },
                    "quantity": purchased_item.quantity,
                }
                line_items.append(line_item)

            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode="payment",
                success_url="http://{}{}".format(host, reverse("success")),
                cancel_url="http://{}{}".format(host, reverse("cancelled")),
                metadata={
                    "order_id": str(order.id),
                },
            )

            # Store the order ID in the session
            # If user cancels the Order we will delete the model object
            self.request.session["order_id"] = str(order.id)

            return redirect(checkout_session.url, code=303)

        elif payment_type == "Cash-On-Delivery":
            create_order("Cash-On-Delivery")
            return redirect("success-cod")


def successView(request):
    order_data = (
        OrderModel.objects.filter(customer=request.user, payment_type="Debit-Card")
        .order_by("-order_date")
        .first()
    )

    data = {"order_data": order_data}
    return render(request, "checkout/success.html", data)


def cancelView(request):
    # Retrieve the cancelled order ID from the session & delete it
    order_id = request.session.get("order_id")

    try:
        cancelled_order = OrderModel.objects.get(pk=order_id)
        # Retrieve cancelled_order respective delivery details and delete it too
        cancelled_order.delivery_information.delete()
        cancelled_order.delete()
    except:
        pass

    return render(request, "checkout/cancel.html")


def successCashOnDeliveryView(request):
    order_data = (
        OrderModel.objects.filter(
            customer=request.user, payment_type="Cash-On-Delivery"
        )
        .order_by("-order_date")
        .first()
    )

    data = {"order_data": order_data}
    return render(request, "checkout/cod.html", data)


@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)

        # print(event)
    except ValueError as e:
        # Invalid payload
        print("Error : ", e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print("Error : ", e)
        # Invalid signature
        return HttpResponse(status=400)

    # handle the checkout.session.completed event i.e. checkout is completed.
    # we can use this to send admin/client a Notification about successful payment of products,etc. + Decrement Products QTY and so on.

    if event["type"] == "checkout.session.completed":
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event["data"]["object"]["id"],
            expand=["line_items"],
        )
        # print("Session : ", session)
        line_items = session.line_items
        # print("Line Items : ", line_items)

        data = {"meta_data": session.metadata}
        fulfill_order(data)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(data):
    # Fetching OrderId
    order_id = data["meta_data"]["order_id"]

    # Updating is_paid of OrderModle to TRUE
    order_data = OrderModel.objects.get(pk=order_id)
    order_data.is_paid = True
    order_data.save()

    # Decrementing Purchased products Quantity
    purchased_data = PurchasedItemModel.objects.filter(order=order_id)

    purchased_qty = 0
    for purchased_item in purchased_data:
        purchased_qty = purchased_item.quantity
        purchased_item.product.quantity = (
            purchased_item.product.quantity - purchased_qty
        )
        purchased_item.product.save()

    print("Debit-Card payment Success ! Source : checkout/views.py/fulfill_order()")
