from django.test import TestCase
from django.urls import reverse, resolve
from customer.models import Customer
from customer.views import view_customer, add_customer, edit_customer, delete_customer

class TestUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data for the tests
        first_name = 'Firstname'
        last_name = 'Lastname'
        username = 'username.test'
        age = '18'
        gender = 'M'
        email = 'test.model@gmail.com'
        civil_status = 'M'
        street = 'testing street'
        barangay = 'testing barangay'
        city = 'testing city'
        birth_date = '1906-06-13'

        cls.customer = Customer.objects.create(
            first_name=first_name, last_name=last_name, username=username,
            age=age, gender=gender, email=email, civil_status=civil_status,
            street=street, barangay=barangay, city=city, birth_date=birth_date
        )
        
    @classmethod
    def tearDownClass(cls):
        # Clean up the test data after all tests are done
        # This method runs once at the end of the test suite
        cls.customer.delete()

    def test_index_url(self):
        url = reverse('customer:index')
        self.assertEqual(resolve(url).func, view_customer)
    
    def test_add_customer_url(self):
        url = reverse('customer:add_customer')
        self.assertEqual(resolve(url).func, add_customer)

    def test_edit_customer_url(self):
        customer = self.customer
        url = reverse('customer:edit_customer', args=[customer.pk])
        self.assertEqual(resolve(url).func, edit_customer)
    
    def test_delete_customer_url(self):
        customer = self.customer
        url = reverse('customer:delete_customer', args=[customer.pk])
        self.assertEqual(resolve(url).func, delete_customer)
