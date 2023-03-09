from django import forms
from SmartShop.models import Shop, ShopData, User

class ShopForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    open = forms.BooleanField()
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    class Meta:
        model = Shop
        fields = ['name', 'owner','data']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['street'].initial = self.instance.data.street
            self.fields['city'].initial = self.instance.data.city
            self.fields['state'].initial = self.instance.data.state
            self.fields['zip_code'].initial = self.instance.data.zip_code

    def save(self, commit=True):
        data = self.instance.data
        data.street = self.cleaned_data['street']
        data.city = self.cleaned_data['city']
        data.state = self.cleaned_data['state']
        data.zip_code = self.cleaned_data['zip_code']
        data.save()
        shop = super().save(commit=commit)
        return shop
    
    def save(self, commit=True):
        data = ShopData.objects.create(
            name = self.cleaned_data['name'],
            owner = self.cleaned_data['owner'],
            open = self.cleaned_data['open'],
            street = self.cleaned_data['street'],
            city = self.cleaned_data['city'],
            state = self.cleaned_data['state'],
            zip_code = self.cleaned_data['zip_code'],
        )
        shop = Shop.objects.create(
            name=self.cleaned_data['name'],
            owner = self.cleaned_data['owner'],
            data=data,
        )
        return shop