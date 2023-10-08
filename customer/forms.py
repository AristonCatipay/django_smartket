from django import forms
from . models import Customer

INPUT_CLASSES = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

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
                'class': INPUT_CLASSES
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'civil_status': forms.Select(attrs={
                'class': INPUT_CLASSES
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
                'class': INPUT_CLASSES,
            }),
        }