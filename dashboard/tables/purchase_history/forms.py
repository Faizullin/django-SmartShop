from django import forms
from SmartShop.models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['shop', 'user', 'goods','quantity','total_price']