from django.shortcuts import render, redirect
from . forms import CustomerForm
from . models import Customer

# Create your views here.

def index(request):
    customers = Customer.objects.all()
    return render(request, 'customer/index.html', {
        'title': 'Customer',
        'customers': customers,
    })

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer:index')
    else:
        form = CustomerForm()
    return render(request, 'customer/form.html', {
        'title': 'Add Customer',
        'form': form,
    })

