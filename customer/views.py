from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from . forms import CustomerForm
from . models import Customer

# Create your views here.

def index(request):
    query = request.GET.get('query', '')
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))

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

def delete_customer(request, primary_key):
    is_delete = True
    customer = get_object_or_404(Customer, id=primary_key)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        customer.delete()
        return redirect('customer:index')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/form.html', {
        'title': 'Delete Customer',
        'form': form,
        'is_delete': is_delete,
    })
