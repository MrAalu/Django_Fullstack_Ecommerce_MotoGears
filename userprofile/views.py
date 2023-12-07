from django.shortcuts import render
from django.views import View
from home.models import *


class ProfileView(View):
    def get(self, request):
        data = {}
        return render(request, "userprofile/dashboard.html", data)


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


class OrderHistoryView(View):
    def get(self, request):
        return render(request, "userprofile/orderhistory.html")


# User's Profile Details
class UserProfileView(View):
    def get(self, request):
        return render(request, "userprofile/profile.html")
