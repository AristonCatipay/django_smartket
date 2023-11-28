from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Customer
from datetime import date

class NumberViewTestCase(TestCase):
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
        url = reverse('number:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'number/index.html')

    def test_add_customer_number(self):
        self.client.force_login(self.user)
        url = reverse('number:add_customer_number')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'number/form.html')

        data = {
            'customer': self.customer.pk,
            'number': '09123456789',
            'network': 'GLOBE',
            'load': 'Go Test 50',
        }

        response = self.client.post(url, data)

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            # print(form.fields['network'].choices)
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)
        # Print data for inspection
        print("\nTest Data Used (Add Customer Number):", data, "\n")

    def tearDown(self):
        # Cleanup after each test
        self.user.delete()
        self.customer.delete()
