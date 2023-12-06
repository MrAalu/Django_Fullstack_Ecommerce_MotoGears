# This View handles the Shipping Details Form
from rest_framework.response import Response
from rest_framework.decorators import api_view
from checkout.models import DeliveryInformationModel


# Stores the Shipping details and then 'Payment Type' Form is Shown to Users
@api_view(["POST"])
def handleShippingForm(request):
    post_data = request.data.get("formObject", {})
    # Extract values from post_data
    full_name = post_data.get("full_name", "")
    address_line1 = post_data.get("address_line1", "")
    address_line2 = post_data.get("address_line2", "")
    city = post_data.get("city", "")
    state = post_data.get("state", "")
    phone_number = post_data.get("phone_number", "")
    email = post_data.get("email", "")

    # User's can have multiple Delivery Details for Multiple Orders
    DeliveryInformationModel.objects.create(
        customer=request.user,
        full_name=full_name,
        address_line1=address_line1,
        address_line2=address_line2,
        city=city,
        state=state,
        phone_number=phone_number,
        email=email,
    )

    return Response({"success": True})
