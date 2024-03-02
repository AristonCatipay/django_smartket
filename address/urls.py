from django.urls import path
from . import views

app_name = 'address'

urlpatterns = [
    path('region/', views.view_region, name='view_region'),
    path('region/create/', views.create_region, name='create_region'),
    path('region/update/<int:primary_key>/', views.update_region, name='update_region'),
    path('region/delete/<int:region_primary_key>/', views.delete_region, name='delete_region'),
]