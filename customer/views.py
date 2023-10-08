from django.shortcuts import render, redirect
from . forms import CustomerForm

# Create your views here.

def index(request):
    return render(request, 'customer/index.html', {
        'title': 'Customer',
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

