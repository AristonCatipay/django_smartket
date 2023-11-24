from django.test import SimpleTestCase
from django.urls import reverse, resolve
from credit.views import index, add_credit_transaction, edit_credit_transaction, mark_transaction_as_paid, credit_product, add_credit_product, edit_credit_product 

class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('credit:index')
        self.assertEquals(resolve(url).func, index)
    
    def test_add_credit_transaction_url(self):
        url = reverse('credit:add_credit_transaction')
        self.assertEquals(resolve(url).func, add_credit_transaction)

    
