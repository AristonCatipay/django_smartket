from django.shortcuts import render, redirect, get_object_or_404
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

def edit_customer(request, primary_key):
    customer = get_object_or_404(Customer, id=primary_key)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:index')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/form.html', {
        'title': 'Edit Customer',
        'form': form,
    })
