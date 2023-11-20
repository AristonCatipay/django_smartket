from django.urls import path
from . import views

app_name = 'credit'

urlpatterns = [
    path('', views.index, name='index'),
    path('transaction/add/', views.add_credit_transaction, name='add_credit_transaction'),
    path('transaction/edit/<int:credit_transaction_primary_key>/', views.edit_credit_transaction, name='edit_credit_transaction'),
    path('product/<int:credit_transaction_primary_key>/', views.credit_product, name='credit_product'),
    path('product/add/<int:credit_transaction_primary_key>/', views.add_credit_product, name='add_credit_product'),
]