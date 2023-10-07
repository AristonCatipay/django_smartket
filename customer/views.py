from django.shortcuts import render
from . forms import CustomerForm

# Create your views here.

def index(request):
    return render(request, 'customer/index.html', {
        'title': 'Customer',
    })

def add_customer(request):
    form = CustomerForm()
    return render(request, 'customer/form.html', {
        'title': 'Add Customer',
        'form': form,
    })

