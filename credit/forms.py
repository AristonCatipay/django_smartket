from django import forms
from .models import Credit_Transaction, Credit_Transaction_Item
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

