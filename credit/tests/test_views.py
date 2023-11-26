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

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/index.html')

    
