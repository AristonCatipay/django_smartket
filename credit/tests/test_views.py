from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from credit.models import Credit_Transaction, Credit_Transaction_Item
from customer.models import Customer
from product.models import Product, Metric_Unit, Category, Color, Size
from datetime import date

class CreditViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            age='30',
            gender='M',
            email='johndoe@example.com',
            street='123 Main St',
            city='Some City',
            birth_date=date(1993, 5, 15),
        )

        self.credit_transaction = Credit_Transaction.objects.create(
            customer=self.customer,
            created_by=self.user,
            due_date=date(2023, 12, 31),
            is_paid=False
        )

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/index.html')
    
    def test_add_credit_transaction_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:add_credit_transaction')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/form.html')

        data = {
            'customer': self.customer.id,
            'due_date': '2023-12-31',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_edit_credit_transaction_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:edit_credit_transaction', kwargs={'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/form.html')

        data = {
            'customer': self.credit_transaction.customer.id,
            'due_date': self.credit_transaction.due_date,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_mark_transaction_as_paid_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:mark_transaction_as_paid', kwargs={'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

        updated_credit_transaction = Credit_Transaction.objects.get(pk=self.credit_transaction.pk)
        self.assertTrue(updated_credit_transaction.is_paid)

    
