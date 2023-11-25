from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from credit.views import index, add_credit_transaction, edit_credit_transaction, mark_transaction_as_paid, credit_product, add_credit_product, edit_credit_product 
from credit.models import Credit_Transaction
from customer.models import Customer

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
        
        # Create a test user
        cls.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    @classmethod
    def tearDownClass(cls):
        # Clean up the test data after all tests are done
        cls.customer.delete()
        cls.user.delete()

    def create_test_credit_transaction(self):
        return Credit_Transaction.objects.create(
            customer=self.customer,
            due_date='2023-11-29',
            created_by=self.user,
        )

    def test_index_url(self):
        url = reverse('credit:index')
        self.assertEquals(resolve(url).func, index)
    
    def test_add_credit_transaction_url(self):
        url = reverse('credit:add_credit_transaction')
        self.assertEquals(resolve(url).func, add_credit_transaction)

    def test_edit_credit_transaction_url(self):
        credit_transaction = self.create_test_credit_transaction()
        url = reverse('credit:edit_credit_transaction', args=[credit_transaction.pk])
        self.assertEquals(resolve(url).func, edit_credit_transaction)
