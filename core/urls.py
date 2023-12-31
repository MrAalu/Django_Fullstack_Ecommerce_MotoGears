from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# from django.views.generic import TemplateView


urlpatterns = [
    path("", include("home.urls")),
    path("shop/", include("shop.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("userprofile.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]


# Serving Images/Media during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
