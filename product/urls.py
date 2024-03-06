from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.view_product, name='view_product'),
    path('create/', views.create_product, name='create_product'),
    path('update/<int:product_primary_key>/', views.update_product, name='update_product'),
    path('delete/<int:product_primary_key>/', views.delete_product, name='delete_product'),
    path('metric/', views.view_metric, name='view_metric'),
    path('metric/create/', views.create_metric, name='create_metric'),
    path('metric/update/<int:metric_primary_key>/', views.update_metric, name='update_metric'),
    path('metric/delete/<int:metric_primary_key>/', views.delete_metric, name='delete_metric'),
    path('category/', views.view_category, name='view_category'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/update/<int:category_primary_key>/', views.update_category, name='update_category'),
    path('category/delete/<int:category_primary_key>/', views.delete_category, name='delete_category'),
    path('color/', views.view_color, name='view_color'),
    path('color/create/', views.create_color, name='create_color'),
    path('color/update/<int:color_primary_key>/', views.update_color, name='update_color'),
    path('color/delete/<int:color_primary_key>/', views.delete_color, name='delete_color'),
    path('size/', views.view_size, name='view_size'),
    path('size/create/', views.create_size, name='create_size'),
    path('size/edit/<int:size_primary_key>/', views.edit_size, name='edit_size'),
    path('size/delete/<int:size_primary_key>/', views.delete_size, name='delete_size'),
]