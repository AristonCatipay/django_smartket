from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import CustomerNumberForm
from . models import Number

@login_required
def index(request):
    query = request.GET.get('query', '')
    customer_numbers = Number.objects.all()

    if query:
        customer_numbers = customer_numbers.filter(number__icontains=query)
    return render(request, 'number/index.html', {
        'title': 'Customer Number',
        'customer_numbers': customer_numbers
    })

@login_required
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

@login_required
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

@login_required
def delete_customer_number(request ,primary_key):
    is_delete = True
    customer_number = get_object_or_404(Number, id=primary_key)
    if request.method == 'POST':
        form = CustomerNumberForm(request.POST, instance=customer_number)
        customer_number.delete()
        return redirect('number:index')
    else: 
        form = CustomerNumberForm(instance=customer_number)
    return render(request, 'number/form.html', {
        'title': 'Delete Number',
        'form': form,
        'is_delete': is_delete,
    })