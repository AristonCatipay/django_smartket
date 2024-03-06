from django.urls import path
from . import views

app_name = 'credit'

urlpatterns = [
    path('', views.view_credit_transaction, name='view_credit_transaction'),
    path('transaction/add/', views.add_credit_transaction, name='add_credit_transaction'),
    path('transaction/edit/<int:credit_transaction_primary_key>/', views.edit_credit_transaction, name='edit_credit_transaction'),
    path('transaction/paid/<int:credit_transaction_primary_key>/', views.mark_transaction_as_paid, name='mark_transaction_as_paid'),
    path('product/<int:credit_transaction_primary_key>/', views.credit_product, name='credit_product'),
    path('product/add/<int:credit_transaction_primary_key>/', views.add_credit_product, name='add_credit_product'),
    path('product/edit/<int:credit_product_primary_key>/<int:credit_transaction_primary_key>/', views.edit_credit_product, name='edit_credit_product'),
]