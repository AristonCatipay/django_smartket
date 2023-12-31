from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import Product, Metric_Unit, Category, Color, Size

class ProductViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.metric_unit = Metric_Unit.objects.create(name='test metric unit')
        self.category = Category.objects.create(name='test category')
        self.color = Color.objects.create(name='test color')
        self.size = Size.objects.create(name='test size')
        self.product = Product.objects.create(
            product_name = 'test product name',
            product_price = 50,
            metric_number = 'test metric number',
            metric_unit = self.metric_unit,
            product_category = self.category,
            product_color = self.color,
            product_size = self.size,
        )

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('product:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'product/index.html')

    def test_add_product_view(self):
        self.client.force_login(self.user)
        url = reverse('product:add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'product_name': self.product.product_name,
            'product_price': self.product.product_price,
            'metric_number': self.product.metric_number,
            'metric_unit': self.metric_unit.pk,
            'product_category': self.category.pk,
            'product_color': self.color.pk,
            'product_size': self.size.pk,
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Add Product):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)
    
    def test_edit_product_view(self):
        self.client.force_login(self.user)
        url = reverse('product:edit_product', kwargs={'product_primary_key': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'product_name': self.product.product_name,
            'product_price': self.product.product_price,
            'metric_number': self.product.metric_number,
            'metric_unit': self.metric_unit.pk,
            'product_category': self.category.pk,
            'product_color': self.color.pk,
            'product_size': self.size.pk,
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Product):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_delete_product_view(self):
        self.client.force_login(self.user)
        url = reverse('product:delete_product', kwargs={'product_primary_key': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'product_name': self.product.product_name,
            'product_price': self.product.product_price,
            'metric_number': self.product.metric_number,
            'metric_unit': self.metric_unit.pk,
            'product_category': self.category.pk,
            'product_color': self.color.pk,
            'product_size': self.size.pk,
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Delete Product):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_metric_view(self):
        self.client.force_login(self.user)
        url = reverse('product:metric')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'product/metric_unit.html')

    def test_add_metric_view(self):
        self.client.force_login(self.user)
        url = reverse('product:add_metric')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.metric_unit.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Product Metric):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)
    
    def test_edit_metric_view(self):
        self.client.force_login(self.user)
        url = reverse('product:edit_metric', kwargs={'metric_primary_key': self.metric_unit.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.metric_unit.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Product Metric):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_category_view(self):
        self.client.force_login(self.user)
        url = reverse('product:category')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'product/category.html')

    def test_add_category_view(self):
        self.client.force_login(self.user)
        url = reverse('product:add_category')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.category.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Product Category):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_edit_category_view(self):
        self.client.force_login(self.user)
        url = reverse('product:edit_category', kwargs={'category_primary_key': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.category.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Product Category):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_color_view(self):
        self.client.force_login(self.user)
        url = reverse('product:color')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'product/color.html')
    
    def test_add_color_view(self):
        self.client.force_login(self.user)
        url = reverse('product:add_color')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.color.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Product Color):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)
    
    def test_edit_color_view(self):
        self.client.force_login(self.user)
        url = reverse('product:edit_color', kwargs={'color_primary_key': self.color.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.color.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Product Color):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_size_view(self):
        self.client.force_login(self.user)
        url = reverse('product:size')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'product/size.html')

    def test_add_size_view(self):
        self.client.force_login(self.user)
        url = reverse('product:add_size')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.size.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Add Product Size):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def test_edit_size_view(self):
        self.client.force_login(self.user)
        url = reverse('product:edit_size', kwargs={'size_primary_key': self.size.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/form.html')

        data = {
            'name': self.size.pk,
        }
        response = self.client.post(url, data)
        print("\nTest Data Used (Edit Product Size):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)

        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        # Cleanup after each test
        self.user.delete()
        self.metric_unit.delete()
        self.category.delete()
        self.color.delete()
        self.size.delete()
        self.product.delete()