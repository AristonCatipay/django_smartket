from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_customer, name='add_customer'),
]