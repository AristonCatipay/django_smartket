from django.urls import path
from . import views

app_name = 'number'

urlpatterns = [
    path('', views.view_number, name='view_number'),
    path('create/', views.create_customer_number, name='create_customer_number'),
    path('update/<int:primary_key>/', views.update_customer_number, name='update_customer_number'),
    path('delete/<int:primary_key>/', views.delete_customer_number, name='delete_customer_number'),
]