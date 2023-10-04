from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('metric/', views.add_metric, name='add_metric'),
]