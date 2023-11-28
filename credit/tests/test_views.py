from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from credit.models import Credit_Transaction, Credit_Transaction_Item
from customer.models import Customer
from product.models import Product, Metric_Unit, Category, Color, Size
from datetime import date

class CreditViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            age='30',
            gender='M',
            email='johndoe@example.com',
            street='123 Main St',
            city='Some City',
            birth_date=date(1993, 5, 15),
        )

        self.credit_transaction = Credit_Transaction.objects.create(
            customer=self.customer,
            created_by=self.user,
            due_date=date(2023, 12, 31),
            is_paid=False
        )

        self.metric_unit = Metric_Unit.objects.create(name='test metric unit')
        self.category = Category.objects.create(name='test category')
        self.color = Color.objects.create(name='test color')
        self.size = Size.objects.create(name='test size')

        self.product = Product.objects.create(
            product_name='Test Product',
            product_price=100,
            metric_unit=self.metric_unit,
            product_category=self.category,
            product_color=self.color,
            product_size=self.size,
        )

        self.credit_product = Credit_Transaction_Item.objects.create(
            credit_transaction=self.credit_transaction,
            product=self.product,
            product_current_price=self.product.product_price
        )

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/index.html')
    
    def test_add_credit_transaction_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:add_credit_transaction')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/form.html')

        data = {
            'customer': self.customer.id,
            'due_date': '2023-12-31',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_edit_credit_transaction_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:edit_credit_transaction', kwargs={'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/form.html')

        data = {
            'customer': self.credit_transaction.customer.id,
            'due_date': self.credit_transaction.due_date,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_mark_transaction_as_paid_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:mark_transaction_as_paid', kwargs={'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

        updated_credit_transaction = Credit_Transaction.objects.get(pk=self.credit_transaction.pk)
        self.assertTrue(updated_credit_transaction.is_paid)

    def test_credit_product_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:credit_product', kwargs={'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/credit_product.html')

    def test_add_credit_product_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:add_credit_product', kwargs={'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/form.html')

        data = {
            'product': self.product.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
    
    def test_edit_credit_product_view(self):
        self.client.force_login(self.user)
        url = reverse('credit:edit_credit_product', kwargs={'credit_product_primary_key': self.credit_product.pk, 'credit_transaction_primary_key': self.credit_transaction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'credit/form.html')

        data = {
            'product': self.product.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        # Cleanup after each test
        self.credit_product.delete()
        self.product.delete()
        self.metric_unit.delete()
        self.category.delete()
        self.color.delete()
        self.size.delete()
        self.credit_transaction.delete()
        self.customer.delete()
        self.user.delete()

        # Ensure clean up after each test.
        credit_product_exists = Credit_Transaction_Item.objects.filter(pk=self.credit_product.pk).exists()
        self.assertFalse(credit_product_exists, "Credit Transaction Item was not deleted.")

        product_exists = Product.objects.filter(pk=self.product.pk).exists()
        self.assertFalse(product_exists, "Product was not deleted.")

        metric_unit_exists = Metric_Unit.objects.filter(pk=self.metric_unit.pk).exists()
        self.assertFalse(metric_unit_exists, "Metric Unit was not deleted.")

        category_exists = Category.objects.filter(pk=self.category.pk).exists()
        self.assertFalse(category_exists, "Category was not deleted.")

        color_exists = Color.objects.filter(pk=self.color.pk).exists()
        self.assertFalse(color_exists, "Color was not deleted.")

        size_exists = Size.objects.filter(pk=self.size.pk).exists()
        self.assertFalse(size_exists, "Size was not deleted.")

        credit_transaction_exists = Credit_Transaction.objects.filter(pk=self.credit_transaction.pk).exists()
        self.assertFalse(credit_transaction_exists, "Credit Transaction was not deleted.")

        customer_exists = Customer.objects.filter(pk=self.customer.pk).exists()
        self.assertFalse(customer_exists, "Customer was not deleted.")

        user_exists = User.objects.filter(pk=self.user.pk).exists()
        self.assertFalse(user_exists, "User was not deleted.")
