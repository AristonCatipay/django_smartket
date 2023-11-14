from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_primary_key>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_primary_key>/', views.delete_product, name='delete_product'),
    path('metric/', views.metric, name='metric'),
    path('metric/add/', views.add_metric, name='add_metric'),
    path('metric/edit/<int:metric_primary_key>/', views.edit_metric, name='edit_metric'),
    path('metric/delete/<int:metric_primary_key>/', views.delete_metric, name='delete_metric'),
    path('category/', views.category, name='category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/edit/<int:category_primary_key>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:category_primary_key>/', views.delete_category, name='delete_category'),
    path('color/', views.color, name='color'),
    path('color/add/', views.add_color, name='add_color'),
    path('color/edit/<int:color_primary_key>/', views.edit_color, name='edit_color'),
    path('color/delete/<int:color_primary_key>/', views.delete_color, name='delete_color'),
    path('size/', views.size, name='size'),
    path('size/add/', views.add_size, name='add_size'),
    path('size/edit/<int:size_primary_key>/', views.edit_size, name='edit_size'),
    path('size/delete/<int:size_primary_key>/', views.delete_size, name='delete_size'),
]