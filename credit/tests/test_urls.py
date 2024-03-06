from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from credit.views import index, create_credit_transaction, update_credit_transaction, mark_transaction_as_paid, credit_product, create_credit_product, edit_credit_product 
from credit.models import Credit_Transaction
from customer.models import Customer
from product.models import Product, Metric_Unit, Size, Category, Color

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
        # This method runs once at the end of the test suite
        cls.customer.delete()
        cls.user.delete()

        Color.objects.filter(name='test_color').delete()
        Size.objects.filter(name='test_size').delete()
        Category.objects.filter(name='test_category').delete()
        Metric_Unit.objects.filter(name='test_unit').delete()
        super().tearDownClass()

    # Methods to create specific test objects
    def create_test_color(self):
        return Color.objects.create(name='test_color')

    def create_test_size(self):
        return Size.objects.create(name='test_size')

    def create_test_category(self):
        return Category.objects.create(name='test_category')

    def create_test_metric_unit(self):
        return Metric_Unit.objects.create(name='test_unit')

    def create_test_credit_product(self):
        color = self.create_test_color()
        size = self.create_test_size()
        category = self.create_test_category()
        metric_unit = self.create_test_metric_unit()

        return Product.objects.create(
            product_name='product_testing', product_price=50,
            metric_number=150, metric_unit=metric_unit,
            product_category=category, product_color=color,
            product_size=size,
        )

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
        self.assertEquals(resolve(url).func, create_credit_transaction)

    def test_edit_credit_transaction_url(self):
        credit_transaction = self.create_test_credit_transaction()
        url = reverse('credit:edit_credit_transaction', args=[credit_transaction.pk])
        self.assertEquals(resolve(url).func, update_credit_transaction)

    def test_mark_transaction_as_paid_url(self):
        credit_transaction = self.create_test_credit_transaction()
        url = reverse('credit:mark_transaction_as_paid', args=[credit_transaction.pk])
        self.assertEquals(resolve(url).func, mark_transaction_as_paid)

    def test_credit_product_url(self):
        credit_transaction = self.create_test_credit_transaction()
        url = reverse('credit:credit_product', args=[credit_transaction.pk])
        self.assertEquals(resolve(url).func, credit_product)

    def test_add_credit_product_url(self):
        credit_transaction = self.create_test_credit_transaction()
        url = reverse('credit:add_credit_product', args=[credit_transaction.pk])
        self.assertEquals(resolve(url).func, create_credit_product)

    def test_edit_credit_product_url(self):
        credit_transaction = self.create_test_credit_transaction()
        credit_product = self.create_test_credit_product()
        url = reverse('credit:edit_credit_product', args=[credit_product.pk, credit_transaction.pk])

        self.assertIsNotNone(credit_transaction)
        self.assertIsNotNone(credit_product)
        self.assertEqual(resolve(url).func, edit_credit_product)