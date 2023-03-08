from django.shortcuts import render
from .models import Shop,ShopData,User,Purchase,Role,Good,GoodType


def main_app(request):
    return render(request,"app.html")
    
