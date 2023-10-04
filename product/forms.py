from django import forms
from . models import Product, Metric_Unit

INPUT_CLASSES = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'metric_number', 'metric_unit', 
                  'product_color', 'product_section', 'product_size')
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'product_price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'metric_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'metric_unit': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'product_color': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'product_section': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'product_size': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }

class AddMetricUnit(forms.ModelForm):
    class Meta:
        model = Metric_Unit
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
