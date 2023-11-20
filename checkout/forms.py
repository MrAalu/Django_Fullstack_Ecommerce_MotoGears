from django import forms
from .models import DeliveryInformationModel


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryInformationModel
        fields = [
            "full_name",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "phone_number",
        ]
