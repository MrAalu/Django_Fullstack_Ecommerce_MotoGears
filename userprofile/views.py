from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request):
        data = {}
        return render(request, "userprofile/dashboard.html", data)


class MyOrdersView(View):
    def get(self, request):
        return render(request, "userprofile/myorders.html")


class OrderHistoryView(View):
    def get(self, request):
        return render(request, "userprofile/orderhistory.html")


# User's Profile Details
class UserProfileView(View):
    def get(self, request):
        return render(request, "userprofile/profile.html")
