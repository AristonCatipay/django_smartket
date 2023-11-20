from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from product.models import Product
from datetime import date

class Credit_Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    due_date = models.DateField()
    paid_at = models.DateField(blank=True, null=True)
    pending_days = models.IntegerField(null=True)

    def mark_as_paid(self):
        if not self.is_paid:  # Ensure it's not already paid
            self.is_paid = True
            self.paid_at = date.today()

            delta = self.paid_at - self.due_date
            self.pending_days = max(delta.days, 0)  # Ensure non-negative days
            self.save()
        

class Credit_Transaction_Item(models.Model):
    credit_transaction = models.ForeignKey(Credit_Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_current_price = models.IntegerField()