from django.urls import path, re_path
from .views import Homepage


urlpatterns = [path("", Homepage.as_view(), name="homepage")]
