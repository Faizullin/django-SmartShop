# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from dashboard import views


app_name = 'dashboard'

urlpatterns = [
    path('shop/', views.shop_index, name='shop_index'),
    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'), 

]
