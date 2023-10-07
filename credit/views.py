from django.shortcuts import render
from . forms import CustomerForm

def index(request):
    return render(request, 'credit/index.html', {
        'title': 'Credit',
    })

def add_customer(request):
    form = CustomerForm()
    return render(request, 'credit/form.html', {
        'title': 'Add Customer',
        'form': form,
    })