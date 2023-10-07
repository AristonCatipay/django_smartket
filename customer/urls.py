from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_customer/', views.add_customer, name='add_customer'),
]