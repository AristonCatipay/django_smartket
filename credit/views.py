from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Credit_Transaction, Credit_Transaction_Item
from .forms import CreditTransactionForm

def index(request):
    credit_transactions = Credit_Transaction.objects.all()
    return render(request, 'credit/index.html', {
        'title': 'Credit',
        'credit_transactions': credit_transactions,
    })

def add_credit_transaction(request):
    if request.method == 'POST':
        form = CreditTransactionForm(request.POST)
        if form.is_valid():
            credit_transaction = form.save(commit=False)
            credit_transaction.created_by = request.user
            credit_transaction.save()
            return redirect('credit:index')
    else:
        form = CreditTransactionForm()
    return render(request, 'credit/form.html', {
        'title': 'Add Credit Transaction',
        'form' : form,
    })

def credit_product(request, credit_transaction_primary_key):
    credit_products = Credit_Transaction_Item.objects.filter(credit_transaction=credit_transaction_primary_key)
    return render(request, 'credit/credit_product.html', {
        'title': 'Credit',
        'credit_products': credit_products,
    })






