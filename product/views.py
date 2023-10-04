from django.shortcuts import render, redirect
from . forms import AddProduct, AddMetricUnit

def index(request):
    return render(request, 'product/index.html', {
        'title': 'Product',
    })

def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = AddProduct()
    return render(request, 'product/add_product.html', {
        'title': 'Add Product', 
        'form': form
    })

def add_metric(request):
    if request.method == 'POST':
        form = AddMetricUnit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = AddMetricUnit()
    return render(request, 'product/add_metric_unit.html', {
        'title': 'Add Metric',
        'form': form,
    })