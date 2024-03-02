from django.urls import path
from . import views

app_name = 'address'

urlpatterns = [
    path('region/', views.view_region, name='view_region'),
    path('region/create/', views.create_region, name='create_region'),
]