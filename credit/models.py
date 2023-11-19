from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from customer.models import Customer
from product.models import Product

class Credit_Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    due_date = models.DateField()
    paid_at = models.DateField(blank=True, null=True)
    payment_delay = models.DurationField(blank=True, null=True)

    def mark_as_paid(self):
        self.is_paid = True
        self.paid_at = timezone.now()
        self.payment_delay = self.paid_at - self.due_date
        self.save()

class Credit_Transaction_Item(models.Model):
    credit_transaction = models.ForeignKey(Credit_Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_current_price = models.IntegerField()