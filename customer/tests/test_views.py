from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class CustomerViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('customer:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'customer/index.html')