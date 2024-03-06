from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from product.models import Product
from .models import Credit_Transaction, Credit_Transaction_Item
from .forms import CreditTransactionForm, CreditTransactionItemForm

@login_required
def view_credit_transaction(request):
    query = request.GET.get('query', '')
    credit_transactions = Credit_Transaction.objects.all()
    
    if query:
        credit_transactions = credit_transactions.filter(Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query))
    return render(request, 'credit/view_credit_transaction.html', {
        'title': 'Credit',
        'credit_transactions': credit_transactions,
    })

@login_required
def create_credit_transaction(request):
    if request.method == 'POST':
        form = CreditTransactionForm(request.POST)
        if form.is_valid():
            credit_transaction = form.save(commit=False)
            credit_transaction.created_by = request.user
            credit_transaction.save()
            messages.success(request, 'Successful! Credit transaction has been created.')
            return redirect('credit:view_credit_transaction')
    else:
        form = CreditTransactionForm()
    return render(request, 'credit/form.html', {
        'title': 'Add Credit Transaction',
        'form' : form,
    })

@login_required
def edit_credit_transaction(request, credit_transaction_primary_key):
    credit_transaction = get_object_or_404(Credit_Transaction, pk=credit_transaction_primary_key)
    if request.method == 'POST':
        form = CreditTransactionForm(request.POST, instance=credit_transaction)
        if form.is_valid():
            form.save()
            messages.success('Successful! Credit transaction has been edited.')
            return redirect('credit:view_credit_transaction')
    else:
        form = CreditTransactionForm(instance=credit_transaction)
    return render(request, 'credit/form.html', {
        'title': 'Edit Credit Transaction',
        'form' : form,
    })

@login_required
def mark_transaction_as_paid(request, credit_transaction_primary_key):
    credit_transaction = get_object_or_404(Credit_Transaction, pk=credit_transaction_primary_key)
    
    if not credit_transaction.is_paid:
        credit_transaction.mark_as_paid()
        credit_transaction.save()
        messages.success('Successful! Credit transaction has been marked as paid.')
    
    return redirect('credit:view_credit_transaction')

@login_required
def credit_product(request, credit_transaction_primary_key):
    credit_products = Credit_Transaction_Item.objects.filter(credit_transaction=credit_transaction_primary_key)
    return render(request, 'credit/credit_product.html', {
        'title': 'Credit',
        'credit_products': credit_products,
        'credit_transaction_primary_key': credit_transaction_primary_key,
    })

@login_required
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
            messages.success('Successful! Credit product has been created.')
            return redirect('credit:credit_product', credit_transaction_primary_key)
    else:
        form = CreditTransactionItemForm()
    return render(request, 'credit/form.html', {
        'title': 'Add Credit Product',
        'form': form,
    })

@login_required
def edit_credit_product(request, credit_product_primary_key, credit_transaction_primary_key):
    credit_product = get_object_or_404(Credit_Transaction_Item, pk=credit_product_primary_key)
    if request.method == 'POST':
        form = CreditTransactionItemForm(request.POST, instance=credit_product)
        if form.is_valid():
            credit_product = form.save(commit=False)

            # Fetch the product from the form data
            product = form.cleaned_data['product']
            product = Product.objects.get(pk=product.id)
            
            credit_product.product = product
            credit_product.product_current_price = product.product_price
            credit_product.save()
            messages.success('Successful! Credit product has been edited.')
            return redirect('credit:credit_product', credit_transaction_primary_key)
    else:
        form = CreditTransactionItemForm(instance=credit_product)
    return render(request, 'credit/form.html', {
        'title': 'Edit Credit Product',
        'form': form,
    })

