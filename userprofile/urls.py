from django.urls import path
from .views import ProfileView, MyOrdersView, OrderHistoryView, UserProfileView

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
    path("myorders/", MyOrdersView.as_view(), name="myorders"),
    path("orderhistory/", OrderHistoryView.as_view(), name="orderhistory"),
    path("userprofile/", UserProfileView.as_view(), name="userprofile"),
]
