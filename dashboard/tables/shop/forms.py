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
        fields = ['name','owner','open','street','city','state','zip_code']
    

    def save(self, commit=True):
        shopData = ShopData.objects.create(
            name = self.cleaned_data['name'],
            owner = self.cleaned_data['owner'],
            open = self.cleaned_data['open'],
            street = self.cleaned_data['street'],
            city = self.cleaned_data['city'],
            state = self.cleaned_data['state'],
            zip_code = self.cleaned_data['zip_code'],
        )
        shop = Shop.objects.create(
            name = self.cleaned_data['name'],
            owner = self.cleaned_data['owner'],
            data = shopData,
        )
        
        return (shop,shopData)
    
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