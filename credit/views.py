from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Credit_Transaction, Credit_Transaction_Item
from .forms import CreditTransactionForm, CreditTransactionItemForm
from product.models import Product

def index(request):
    query = request.GET.get('query', '')
    credit_transactions = Credit_Transaction.objects.all()
    
    if query:
        credit_transactions = credit_transactions.filter(Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query))
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

def edit_credit_transaction(request, credit_transaction_primary_key):
    credit_transaction = get_object_or_404(Credit_Transaction, pk=credit_transaction_primary_key)
    if request.method == 'POST':
        form = CreditTransactionForm(request.POST, instance=credit_transaction)
        if form.is_valid():
            form.save()
            return redirect('credit:index')
    else:
        form = CreditTransactionForm(instance=credit_transaction)
    return render(request, 'credit/form.html', {
        'title': 'Edit Credit Transaction',
        'form' : form,
    })

def credit_product(request, credit_transaction_primary_key):
    credit_products = Credit_Transaction_Item.objects.filter(credit_transaction=credit_transaction_primary_key)
    return render(request, 'credit/credit_product.html', {
        'title': 'Credit',
        'credit_products': credit_products,
        'credit_transaction_primary_key': credit_transaction_primary_key,
    })

def add_credit_product(request, credit_transaction_primary_key):
    if request.method == 'POST':
        form = CreditTransactionItemForm(request.POST)
        if form.is_valid():
            credit_product = form.save(commit=False)

            # Fetch the product from the form data
            product = form.cleaned_data['product']

            product = Product.objects.get(pk=product.id)
            credit_transaction = Credit_Transaction.objects.get(pk=credit_transaction_primary_key)

            credit_product.credit_transaction = credit_transaction
            credit_product.product = product
            credit_product.product_current_price = product.product_price

            credit_product.save()
            return redirect('credit:credit_product', credit_transaction_primary_key)
    else:
        form = CreditTransactionItemForm()
    return render(request, 'credit/form.html', {
        'title': 'Add Credit Product',
        'form': form,
    })






