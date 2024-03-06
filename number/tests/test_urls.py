from django.test import TestCase
from django.urls import reverse, resolve
from customer.models import Customer
from number.models import Number
from number.views import view_number, add_customer_number, edit_customer_number, delete_customer_number

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

    def create_test_customer_number(self):
        return Number.objects.create(
            customer=self.customer,
            number='09123214567',
            load='Go Testing',
        )

    def test_index_url(self):
        url = reverse('number:index')
        self.assertEqual(resolve(url).func, view_number)
    
    def test_add_customer_number_url(self):
        url = reverse('number:add_customer_number')
        self.assertEqual(resolve(url).func, add_customer_number)

    def test_edit_customer_number_url(self):
        number = self.create_test_customer_number()
        url = reverse('number:edit_customer_number', args=[number.pk])
        self.assertEqual(resolve(url).func, edit_customer_number)
    
    def test_delete_customer_url(self):
        number = self.create_test_customer_number()
        url = reverse('number:delete_customer_number', args=[number.pk])
        self.assertEqual(resolve(url).func, delete_customer_number)

    
