from django.urls import path, re_path
from . import views
from dashboard.urls import urlpatterns as home_urlpatterns
from authentication.urls import urlpatterns as auth_urlpatterns

app_name = 'smartshop'

urlpatterns = [
    # path('',views.index,name='index'),
    # path('create',views.create,name="create"),
    re_path(r'^.*\.*', views.main_app, name='main_app'),

    #path('dashboard/', views.book_list, name='book_list'),
    #path('chapters/<int:pk>/', views.chapter_detail, name='chapter_detail'),
]