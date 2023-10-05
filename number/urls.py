from django.urls import path
from . import views

app_name = 'number'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_customer_number, name='add_customer_number'),
    path('edit/<int:primary_key>/', views.edit_customer_number, name='edit_customer_number'),
]