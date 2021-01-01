from django import forms
from django.forms import ModelForm, CharField
from .models import BillOfSale
from django.utils import timezone

class BillOfSaleForm(ModelForm):
    class Meta:
        model = BillOfSale
        fields = ['seller_name', 'seller_address', 'seller_city',
        'seller_state', 'seller_zip', 'buyer_name', 'buyer_address', 'buyer_city', 'buyer_state',
        'buyer_zip', 'properties', 'price', 'sale_date']


class BillOfSaleForm01(ModelForm):
    class Meta:
        model = BillOfSale
        fields = ['seller_name', 'seller_address', 'seller_city',
        'seller_state', 'seller_zip']


class BillOfSaleForm02(ModelForm):
    class Meta:
        model = BillOfSale
        fields = ['buyer_name', 'buyer_address', 'buyer_city',
        'buyer_state', 'buyer_zip']


class BillOfSaleForm03(ModelForm):
    class Meta:
        model = BillOfSale
        fields = ['properties', 'price', 'sale_date']

    