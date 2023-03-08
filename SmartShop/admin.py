from django.contrib import admin
from .models import Shop,ShopData,User,Purchase,Role,Good,GoodType

# Register your models here.
tmp_models = [Shop,ShopData,Purchase,Role,Good,GoodType]
for tmp_model in tmp_models:
    admin.site.register(tmp_model)