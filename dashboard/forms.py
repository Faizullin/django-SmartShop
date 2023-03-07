from django import forms
from SmartShop.models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'owner', 'address','data']
