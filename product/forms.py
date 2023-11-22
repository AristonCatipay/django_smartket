from django import forms
from . models import Product, Metric_Unit, Category, Color, Size

INPUT_CLASSES = 'rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
SELECT_AREA = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
TEXT_AREA = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
CHECKBOX = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'metric_number', 'metric_unit', 
                  'product_color', 'product_category', 'product_size')
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
                'class': SELECT_AREA
            }),
            'product_color': forms.Select(attrs={
                'class': SELECT_AREA
            }),
            'product_category': forms.Select(attrs={
                'class': SELECT_AREA
            }),
            'product_size': forms.Select(attrs={
                'class': SELECT_AREA
            }),
        }

class MetricUnitForm(forms.ModelForm):
    class Meta:
        model = Metric_Unit
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }