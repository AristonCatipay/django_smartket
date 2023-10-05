from django.shortcuts import render, redirect, get_object_or_404
from . forms import AddCustomerNumber, EditCustomerNumber
from . models import Number

def index(request):
    customer_numbers = Number.objects.all()
    return render(request, 'number/index.html', {
        'title': 'Customer Number',
        'customer_numbers': customer_numbers
    })

def add_customer_number(request):
    if request.method == 'POST':
        form = AddCustomerNumber(request.POST)

        if form.is_valid():
            form.save()
            return redirect('number:index')
    else:
        form = AddCustomerNumber()
    return render(request, 'number/form.html', {
        'title': 'Add Customer Number',
        'form': form,
    })

def edit_customer_number(request, primary_key):
    number_id = get_object_or_404(Number, id=primary_key)
    if request.method == 'POST':
        form = EditCustomerNumber(request.POST, instance=number_id)

        if form.is_valid():
            form.save()
            return redirect('number:index')
    else:
        form = EditCustomerNumber(instance=number_id)
    return render(request, 'number/form.html', {
        'title': 'Edit Number',
        'form': form,
    })

def delete_customer_number(request ,primary_key):
    customer_number = get_object_or_404(Number, id=primary_key)
    customer_number.delete()
    return redirect('number:index')