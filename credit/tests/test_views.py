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

    
