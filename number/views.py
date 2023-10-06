from django.shortcuts import render, redirect, get_object_or_404
from . forms import CustomerNumberForm
from . models import Number

def index(request):
    customer_numbers = Number.objects.all()
    return render(request, 'number/index.html', {
        'title': 'Customer Number',
        'customer_numbers': customer_numbers
    })

def add_customer_number(request):
    if request.method == 'POST':
        form = CustomerNumberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('number:index')
    else:
        form = CustomerNumberForm()
    return render(request, 'number/form.html', {
        'title': 'Add Customer Number',
        'form': form,
    })

def edit_customer_number(request, primary_key):
    number_id = get_object_or_404(Number, id=primary_key)
    if request.method == 'POST':
        form = CustomerNumberForm(request.POST, instance=number_id)

        if form.is_valid():
            form.save()
            return redirect('number:index')
    else:
        form = CustomerNumberForm(instance=number_id)
    return render(request, 'number/form.html', {
        'title': 'Edit Number',
        'form': form,
    })

def delete_customer_number(request ,primary_key):
    is_delete = True
    customer_number = get_object_or_404(Number, id=primary_key)
    if request.method == 'POST':
        form = CustomerNumberForm(request.POST, instance=customer_number)
        customer_number.delete()
    else: 
        form = CustomerNumberForm(instance=customer_number)
    return render(request, 'number/form.html', {
        'title': 'Delete Number',
        'form': form,
        'is_delete': is_delete,
    })