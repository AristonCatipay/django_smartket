from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from . forms import CustomerForm
from . models import Customer

@login_required
def view_customer(request):
    query = request.GET.get('query', '')
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))

    return render(request, 'customer/view_customer.html', {
        'title': 'Customer',
        'customers': customers,
    })

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success('Successful! Customer details has been created.')
            return redirect('customer:index')
    else:
        form = CustomerForm()
    return render(request, 'customer/form.html', {
        'title': 'Add Customer',
        'form': form,
    })

@login_required
def edit_customer(request, primary_key):
    customer = get_object_or_404(Customer, id=primary_key)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success('Successful! Customer details has been edited.')
            return redirect('customer:index')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/form.html', {
        'title': 'Edit Customer',
        'form': form,
    })

@login_required
def delete_customer(request, primary_key):
    is_delete = True
    customer = get_object_or_404(Customer, id=primary_key)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        customer.delete()
        messages.success('Successful! Customer details has been deleted.')
        return redirect('customer:index')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/form.html', {
        'title': 'Delete Customer',
        'form': form,
        'is_delete': is_delete,
    })
