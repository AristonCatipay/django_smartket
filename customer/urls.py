from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('', views.view_customer, name='view_customer'),
    path('create/', views.create_customer, name='create_customer'),
    path('edit/<int:primary_key>/', views.edit_customer, name='edit_customer'),
    path('delete/<int:primary_key>/', views.delete_customer, name='delete_customer'),
]