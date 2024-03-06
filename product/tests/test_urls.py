from django.test import TestCase
from django.urls import reverse, resolve
from customer.models import Customer
from product.models import Product, Color, Category, Size, Metric_Unit
from product.views import index, create_product, update_product, delete_product, view_metric, create_metric, update_metric, delete_metric, category, create_category, update_category, delete_category, view_color, create_color, update_color, delete_color, size, add_size, edit_size, delete_size

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

    def create_test_product(self):
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

    def test_index_url(self):
        url = reverse('product:index')
        self.assertEqual(resolve(url).func, index)

    def test_add_product_url(self):
        url = reverse('product:add_product')
        self.assertEquals(resolve(url).func, create_product)
    
    def test_edit_product_url(self):
        product = self.create_test_product()
        url = reverse('product:edit_product', args=[product.pk])
        self.assertEquals(resolve(url).func, update_product)

    def test_delete_product_url(self):
        product = self.create_test_product()
        url = reverse('product:delete_product', args=[product.pk])
        self.assertEquals(resolve(url).func, delete_product)
    
    def test_metric_url(self):
        url = reverse('product:metric')
        self.assertEqual(resolve(url).func, view_metric)
    
    def test_add_metric_url(self):
        url = reverse('product:add_metric')
        self.assertEquals(resolve(url).func, create_metric)

    def test_edit_metric_url(self):
        metric = self.create_test_metric_unit()
        url = reverse('product:edit_metric', args=[metric.pk])
        self.assertEquals(resolve(url).func, update_metric)

    def test_delete_metric_url(self):
        metric = self.create_test_metric_unit()
        url = reverse('product:delete_metric', args=[metric.pk])
        self.assertEquals(resolve(url).func, delete_metric)
    
    def test_category_url(self):
        url = reverse('product:category')
        self.assertEqual(resolve(url).func, category)

    def test_add_category_url(self):
        url = reverse('product:add_category')
        self.assertEquals(resolve(url).func, create_category)
    
    def test_edit_category_url(self):
        category = self.create_test_category()
        url = reverse('product:edit_category', args=[category.pk])
        self.assertEquals(resolve(url).func, update_category)
    
    def test_delete_category_url(self):
        category = self.create_test_category()
        url = reverse('product:delete_category', args=[category.pk])
        self.assertEquals(resolve(url).func, delete_category)

    def test_color_url(self):
        url = reverse('product:color')
        self.assertEqual(resolve(url).func, view_color)

    def test_add_color_url(self):
        url = reverse('product:add_color')
        self.assertEquals(resolve(url).func, create_color)
    
    def test_edit_color_url(self):
        color = self.create_test_color()
        url = reverse('product:edit_color', args=[color.pk])
        self.assertEquals(resolve(url).func, update_color)

    def test_delete_color_url(self):
        color = self.create_test_color()
        url = reverse('product:delete_color', args=[color.pk])
        self.assertEquals(resolve(url).func, delete_color)

    def test_size_url(self):
        url = reverse('product:size')
        self.assertEqual(resolve(url).func, size)
    
    def test_add_size_url(self):
        url = reverse('product:add_size')
        self.assertEquals(resolve(url).func, add_size)

    def test_edit_size_url(self):
        size = self.create_test_size()
        url = reverse('product:edit_size', args=[size.pk])
        self.assertEquals(resolve(url).func, edit_size)

    def test_delete_size_url(self):
        size = self.create_test_size()
        url = reverse('product:delete_size', args=[size.pk])
        self.assertEquals(resolve(url).func, delete_size)