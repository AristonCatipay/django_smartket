from django import forms
from . models import Customer

INPUT_CLASSES = 'rounded-r-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
SELECT_AREA = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
TEXT_AREA = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
CHECKBOX = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'age', 
                  'gender', 'email', 'civil_status', 
                  'street', 'barangay', 'city', 'birth_date')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }), 
            'username': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'age': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gender': forms.Select(attrs={
                'class': SELECT_AREA
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'civil_status': forms.Select(attrs={
                'class': SELECT_AREA
            }),
            'street': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'barangay': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'birth_date': forms.SelectDateWidget(years=range(1900, 2999), attrs={
                'class': SELECT_AREA,
            }),
        }