from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from home.models import ProductModel


class ViewProduct(View):
    def get(self, request, product_id):
        product = get_object_or_404(ProductModel, id=product_id)

        return render(
            request,
            "shop/view_product.html",
            {"product": product},
        )
