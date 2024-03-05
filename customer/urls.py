from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('', views.view_customer, name='view_customer'),
    path('create/', views.create_customer, name='create_customer'),
    path('update/<int:customer_primary_key>/', views.update_customer, name='update_customer'),
    path('delete/<int:customer_primary_key>/', views.delete_customer, name='delete_customer'),
]