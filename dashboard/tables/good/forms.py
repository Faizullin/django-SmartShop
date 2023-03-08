from django import forms
from SmartShop.models import Good

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['name', 'description', 'price','type']