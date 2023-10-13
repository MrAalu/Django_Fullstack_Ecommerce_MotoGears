from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import ProductModel
from decimal import Decimal


class Homepage(View):
    def get(self, request):
        # Fetch products with Discounts
        discount_products = ProductModel.objects.filter(sale_price__isnull=False)

        # Calculate discount percentage for each product
        for product in discount_products:
            discount_percentage = (
                (product.original_price - product.sale_price) / product.original_price
            ) * 100

            # Decimal() to make Precise Decimal Conversion, Quantize() to make decimal places of 2
            product.discount_percentage = Decimal(discount_percentage).quantize(
                Decimal("0.00")
            )

        data = {"discount_products": discount_products}

        return render(request, "home/index.html", data)
