from django.urls import path
from . import views

app_name = 'credit'

urlpatterns = [
    path('', views.view_credit_transaction, name='view_credit_transaction'),
    path('transaction/create/', views.create_credit_transaction, name='create_credit_transaction'),
    path('transaction/update/<int:credit_transaction_primary_key>/', views.update_credit_transaction, name='update_credit_transaction'),
    path('transaction/update/paid/<int:credit_transaction_primary_key>/', views.mark_transaction_as_paid, name='mark_transaction_as_paid'),
    path('product/<int:credit_transaction_primary_key>/', views.view_credit_product, name='view_credit_product'),
    path('product/create/<int:credit_transaction_primary_key>/', views.create_credit_product, name='create_credit_product'),
    path('product/edit/<int:credit_product_primary_key>/<int:credit_transaction_primary_key>/', views.edit_credit_product, name='edit_credit_product'),
]