from django.urls import path
from . import views

app_name = 'number'

urlpatterns = [
    path('', views.index, name='index'),
]