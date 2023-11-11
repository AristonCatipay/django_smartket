from django.shortcuts import render, redirect, get_object_or_404
from . forms import ProductForm, MetricUnitForm
from . models import Product, Metric_Unit

def index(request):
    query = request.GET.get('query', '')
    products = Product.objects.all()

    if query:
        products = products.filter(product_name__icontains=query)

    return render(request, 'product/index.html', {
        'title': 'Product',
        'products': products,
        'query': query,
    })

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = ProductForm()
    return render(request, 'product/form.html', {
        'title': 'Add Product', 
        'form': form
    })

def edit_product(request, primary_key):
    product = get_object_or_404(Product, id=primary_key)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/form.html', {
        'title': 'Edit Product',
        'form': form, 
    })

def delete_product(request, primary_key):
    model = 'Product'
    is_delete = True
    product = get_object_or_404(Product, id=primary_key)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        product.delete()
        return redirect('product:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/form.html', {
        'title': 'Delete Product',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })

def metric(request):
    metric_units = Metric_Unit.objects.all()
    return render(request, 'product/index_metric_unit.html', {
        'title': 'Metric',
        'metric_units': metric_units,
    })

def add_metric(request):
    if request.method == 'POST':
        form = MetricUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:metric')
    else:
        form = MetricUnitForm()
    return render(request, 'product/form.html', {
        'title': 'Add Metric',
        'form': form,
    })


def edit_metric(request, primary_key):
    metric = get_object_or_404(Metric_Unit, id=primary_key)
    if request.method == 'POST':
        form = MetricUnitForm(request.POST, instance=metric)
        if form.is_valid():
            form.save()
            return redirect('product:metric')
    else:
        form = MetricUnitForm(instance=metric)
    
    return render(request, 'product/form.html', {
        'title': 'Edit Metric', 
        'form': form,
    })


def delete_metric(request, primary_key):
    model = 'Metric Unit'
    is_delete = True
    metric = get_object_or_404(Metric_Unit, id=primary_key)
    if request.method == 'POST':
        form = MetricUnitForm(request.POST, instance=metric)
        metric.delete()
        return redirect('product:metric')
    else:
        form = MetricUnitForm(instance=metric)
    return render(request ,'product/form.html', {
        'title': 'Delete Product',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })