from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Customer

class CustomerViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('customer:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'customer/index.html')

    def test_add_customer(self):
        self.client.force_login(self.user)
        url = reverse('customer:add_customer')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/form.html')

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'age': '30',
            'gender': 'M',
            'email': 'johndoe@example.com',
            'civil_status': 'S',
            'street': '123 Main St',
            'barangay': 'Some Barangay',
            'city': 'Some City',
            'birth_date': '1993-05-15',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Print data for inspection
        print("\nTest Data Used:", data, "\n")
        

    def tearDown(self):
        # Cleanup after each test
        self.user.delete()
