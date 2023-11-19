from django.shortcuts import render
from .models import Credit_Transaction, Credit_Transaction_Item

def index(request):
    credit_transactions = Credit_Transaction.objects.all()
    return render(request, 'credit/index.html', {
        'title': 'Credit',
        'credit_transactions': credit_transactions,
    })







