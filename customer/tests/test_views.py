from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Customer
from datetime import date

class CustomerViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            username='john.doe',
            age='30',
            gender='M',
            email='johndoe@gmail.com',
            barangay='Some Barangay',
            street='Some Street',
            city='Some City',
            birth_date=date(1993, 5, 15),
        )

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
            'first_name': self.customer.first_name,
            'last_name': self.customer.last_name,
            'username': 'unique.username',
            'age': self.customer.age,
            'gender': self.customer.gender,
            'email': 'unique.email@gmail.com',
            'civil_status': self.customer.civil_status,
            'street': self.customer.street,
            'barangay': self.customer.barangay,
            'city': self.customer.city,
            'birth_date': self.customer.birth_date,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Print data for inspection
        print("\nTest Data Used (Add Customer):", data, "\n")
    
    def test_edit_customer(self):
        self.client.force_login(self.user)
        url = reverse('customer:edit_customer', kwargs={'primary_key': self.customer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/form.html')

        data = {
            'first_name': self.customer.first_name,
            'last_name': self.customer.last_name,
            'username': self.customer.username,
            'age': self.customer.age,
            'gender': self.customer.gender,
            'email': self.customer.email,
            'civil_status': self.customer.civil_status,
            'street': self.customer.street,
            'barangay': self.customer.barangay,
            'city': self.customer.city,
            'birth_date': self.customer.birth_date,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Print data for inspection
        print("\nTest Data Used (Edit Customer):", data, "\n")
    
    def test_delete_customer(self):
        self.client.force_login(self.user)
        url = reverse('customer:delete_customer', kwargs={'primary_key': self.customer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/form.html')

        data = {
            'first_name': self.customer.first_name,
            'last_name': self.customer.last_name,
            'username': self.customer.username,
            'age': self.customer.age,
            'gender': self.customer.gender,
            'email': self.customer.email,
            'civil_status': self.customer.civil_status,
            'street': self.customer.street,
            'barangay': self.customer.barangay,
            'city': self.customer.city,
            'birth_date': self.customer.birth_date,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Print data for inspection
        print("\nTest Data Used (Delete Customer):", data, "\n")

    def tearDown(self):
        # Cleanup after each test
        self.user.delete()
        self.customer.delete()

        # Ensure clean up after each test.
        customer = Customer.objects.filter(pk=self.customer.pk).exists()
        self.assertFalse(customer, "Customer Item was not deleted.")

        user_exists = User.objects.filter(pk=self.user.pk).exists()
        self.assertFalse(user_exists, "User was not deleted.")