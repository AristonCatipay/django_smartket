from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:primary_key>/', views.edit_product, name='edit_product'),
    path('delete/<int:primary_key>/', views.delete_product, name='delete_product'),
    path('metric/', views.metric, name='metric'),
    path('add_metric/', views.add_metric, name='add_metric'),
    path('edit_metric/<int:primary_key>/', views.edit_metric, name='edit_metric'),
    path('delete_metric/<int:primary_key>/', views.delete_metric, name='delete_metric'),
    path('category/', views.category, name='category'),
]