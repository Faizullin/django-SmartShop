from django.contrib import admin
from .models import Shop,ShopData,User,Purchase,Good,GoodType

# Register your models here.
tmp_models = [Shop,ShopData,Purchase,Good,GoodType]
for tmp_model in tmp_models:
    admin.site.register(tmp_model)