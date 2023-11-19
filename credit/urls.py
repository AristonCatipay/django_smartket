from django.urls import path
from . import views

app_name = 'credit'

urlpatterns = [
    path('', views.index, name='index'),
    path('transaction/add/', views.add_credit_transaction, name='add_credit_transaction'),
    path('product/<int:credit_transaction_primary_key>', views.credit_product, name='credit_product'),
]