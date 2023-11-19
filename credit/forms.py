from django import forms
from .models import Credit_Transaction, Credit_Transaction_Item
from product.models import Product
import datetime

INPUT_CLASSES = 'block w-full p-2 text-sm text-gray-100 border border-violet-300 rounded-lg bg-gray-700 focus:ring-blue-500 focus:border-blue-500'
today = datetime.date.today()

class CreditTransactionForm(forms.ModelForm):
    class Meta:
        model = Credit_Transaction
        fields = ['customer', 'due_date']
        widgets = {
            'customer': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'due_date': forms.SelectDateWidget(years=range(today.year, 2999), attrs={
                'class': INPUT_CLASSES,
            }),
        }

class CreditTransactionItemForm(forms.ModelForm):
    class Meta:
        model = Credit_Transaction_Item
        fields = ['product']
        widgets = {
            'product': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the choices for the product field
        self.fields['product'].widget.choices = [(product.id, product.product_name) for product in Product.objects.all()]
