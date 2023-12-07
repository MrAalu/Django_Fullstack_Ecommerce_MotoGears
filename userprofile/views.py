from django.shortcuts import render
from django.views import View
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404


@method_decorator(login_required(login_url="/accounts/login/"), name="dispatch")
class ProfileView(View):
    def get(self, request):
        data = {}
        return render(request, "userprofile/dashboard.html", data)


@method_decorator(login_required(login_url="/accounts/login/"), name="dispatch")
class MyOrdersView(View):
    def get(self, request):
        excluded_statuses = ["Delivered", "Cancelled"]
        myorders = (
            OrderModel.objects.filter(customer_id=request.user)
            .exclude(order_status__in=excluded_statuses)
            .order_by("-order_date")
        )

        data = {"myorders": myorders}

        for order in myorders:
            purchased_items = PurchasedItemModel.objects.filter(order=order)
            order.purchased_items = purchased_items

        return render(request, "userprofile/myorders.html", data)


@method_decorator(login_required(login_url="/accounts/login/"), name="dispatch")
class OrderHistoryView(View):
    def get(self, request):
        excluded_statuses = ["Processing", "Shipping"]
        myorders = (
            OrderModel.objects.filter(customer_id=request.user)
            .exclude(order_status__in=excluded_statuses)
            .order_by("-order_date")
        )

        data = {"myorders": myorders}

        for order in myorders:
            purchased_items = PurchasedItemModel.objects.filter(order=order)
            order.purchased_items = purchased_items

        return render(request, "userprofile/orderhistory.html", data)


# User's Profile Details
@method_decorator(login_required(login_url="/accounts/login/"), name="dispatch")
class UserProfileView(View):
    def get(self, request):
        user_data = get_object_or_404(User, pk=request.user.id)
        data = {"user_data": user_data}
        return render(request, "userprofile/profile.html", data)
