from django.urls import path
from . import views

urlpatterns = [
    path('good/', views.good_index, name='good_index'),
    path('good/create', views.good_create, name='good_create'),
    path('good/update/<int:pk>', views.good_edit, name='good_edit'),
]