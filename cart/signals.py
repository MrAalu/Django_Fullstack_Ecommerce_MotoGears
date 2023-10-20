from django.db.models.signals import pre_save
from django.dispatch import receiver
from home.models import ProductModel, OrderItemModel


# Function that Changes all cart items price to updated price
# Check if Original Price / Sale Price to be put
@receiver(pre_save, sender=ProductModel)
def update_cart_items_prices(sender, instance, **kwargs):
    # Retrieving the old model instance of Product
    try:
        old_instance = ProductModel.objects.get(pk=instance.pk)
    except ProductModel.DoesNotExist:
        old_instance = None

    # Old_Instance (Model) exists
    if old_instance is not None:
        if (
            instance.original_price != old_instance.original_price
            or instance.sale_price != old_instance.sale_price
        ):
            # check if product has sale price or original price
            if instance.sale_price is None:
                product_price = instance.original_price
            else:
                product_price = instance.sale_price

            all_carts = OrderItemModel.objects.filter(product=instance)

            # now change the price of cart item
            for cart in all_carts:
                cart.price = product_price
                cart.save()
