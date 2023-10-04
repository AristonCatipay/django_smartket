from django.shortcuts import render, redirect
from . forms import AddProduct, AddMetricUnit
from . models import Product, Metric_Unit

def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {
        'title': 'Product',
        'products': products,
    })

def metric(request):
    metric_units = Metric_Unit.objects.all()
    return render(request, 'product/index_metric_unit.html', {
        'title': 'Metric',
        'metric_units': metric_units,
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