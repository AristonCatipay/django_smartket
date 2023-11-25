from django.test import TestCase
from django.urls import reverse, resolve
from customer.models import Customer
from product.models import Product, Color, Category, Size, Metric_Unit
from product.views import index, add_product, edit_product, delete_product, metric, add_metric, edit_metric, delete_metric, category, add_category, edit_category, delete_category, color, add_color, edit_color, delete_color, size, add_size, edit_size, delete_size

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
        url = reverse('product:index')
        self.assertEqual(resolve(url).func, index)

    def test_add_product_url(self):
        url = reverse('product:add_product')
        self.assertEquals(resolve(url).func, add_product)
    
    def test_metric_url(self):
        url = reverse('product:metric')
        self.assertEqual(resolve(url).func, metric)
    
    def test_add_metric_url(self):
        url = reverse('product:add_metric')
        self.assertEquals(resolve(url).func, add_metric)
    
    def test_category_url(self):
        url = reverse('product:category')
        self.assertEqual(resolve(url).func, category)

    def test_add_category_url(self):
        url = reverse('product:add_category')
        self.assertEquals(resolve(url).func, add_category)

    def test_color_url(self):
        url = reverse('product:color')
        self.assertEqual(resolve(url).func, color)

    def test_add_color_url(self):
        url = reverse('product:add_color')
        self.assertEquals(resolve(url).func, add_color)

    def test_size_url(self):
        url = reverse('product:size')
        self.assertEqual(resolve(url).func, size)
    
    def test_add_size_url(self):
        url = reverse('product:add_size')
        self.assertEquals(resolve(url).func, add_size)