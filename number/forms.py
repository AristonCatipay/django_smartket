from django import forms
from . models import Number

INPUT_CLASSES = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class AddCustomerNumber(forms.ModelForm):
    class Meta:
        model = Number
        fields = ('name', 'number', 'network', 'load')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'network': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'load': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            })
        }


class EditCustomerNumber(forms.ModelForm):
    class Meta:
        model = Number
        fields = ('name', 'number', 'network', 'load')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'network': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'load': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            })
        }