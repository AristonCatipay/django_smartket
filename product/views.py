from django.shortcuts import render, redirect, get_object_or_404
from . forms import AddProduct, AddMetricUnit, EditProduct
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

def edit_product(request, primary_key):
    product = get_object_or_404(Product, id=primary_key)
    if request.method == 'POST':
        form = EditProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = EditProduct(instance=product)
    return render(request, 'product/edit_product.html', {
        'title': 'Edit Product',
        'form': form, 
    })