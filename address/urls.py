from django.urls import path
from . import views

app_name = 'address'

urlpatterns = [
    path('region/', views.view_region, name='view_region'),
]