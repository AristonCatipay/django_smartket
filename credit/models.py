from django.db import models
from customer.models import Customer
from product.models import Product

class Credited_Product(models.Model):
    product = models.ForeignKey(Product, related_name='product_id', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='customer_id_credit', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



