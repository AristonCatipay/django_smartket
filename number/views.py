from django.shortcuts import render, redirect
from . forms import AddCustomerNumber

def index(request):
    return render(request, 'number/index.html', {
        'title': 'Customer Number'
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