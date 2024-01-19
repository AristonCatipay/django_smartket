from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import ProductForm, MetricUnitForm, CategoryForm, ColorForm, SizeForm
from . models import Product, Metric_Unit, Category, Color, Size

@login_required
def index(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.all()
    
    if query:
        products = products.filter(product_name__icontains=query)
    
    if category_id:
        products = products.filter(product_category = category_id)

    return render(request, 'product/index.html', {
        'title': 'Product',
        'products': products,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product details has been created.')
            return redirect('product:index')
    else:
        form = ProductForm()
    return render(request, 'product/form.html', {
        'title': 'Add Product', 
        'form': form
    })

@login_required
def edit_product(request, product_primary_key):
    product = get_object_or_404(Product, id=product_primary_key)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product details has been edited.')
            return redirect('product:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/form.html', {
        'title': 'Edit Product',
        'form': form, 
    })

@login_required
def delete_product(request, product_primary_key):
    model = 'Product'
    is_delete = True
    product = get_object_or_404(Product, id=product_primary_key)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        product.delete()
        messages.success(request, 'Successful! Product details has been deleted.')
        return redirect('product:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/form.html', {
        'title': 'Delete Product',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })

@login_required
def metric(request):
    metric_units = Metric_Unit.objects.all()
    return render(request, 'product/metric_unit.html', {
        'title': 'Metric',
        'metric_units': metric_units,
    })

@login_required
def add_metric(request):
    if request.method == 'POST':
        form = MetricUnitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product metric has been added.')
            return redirect('product:metric')
    else:
        form = MetricUnitForm()
    return render(request, 'product/form.html', {
        'title': 'Add Metric',
        'form': form,
    })

@login_required
def edit_metric(request, metric_primary_key):
    metric = get_object_or_404(Metric_Unit, id=metric_primary_key)
    if request.method == 'POST':
        form = MetricUnitForm(request.POST, instance=metric)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product metric has been edited.')
            return redirect('product:metric')
    else:
        form = MetricUnitForm(instance=metric)
    
    return render(request, 'product/form.html', {
        'title': 'Edit Metric', 
        'form': form,
    })

@login_required
def delete_metric(request, metric_primary_key):
    model = 'Metric Unit'
    is_delete = True
    metric = get_object_or_404(Metric_Unit, id=metric_primary_key)
    if request.method == 'POST':
        form = MetricUnitForm(request.POST, instance=metric)
        metric.delete()
        messages.success(request, 'Successful! Product metric has been deleted.')
        return redirect('product:metric')
    else:
        form = MetricUnitForm(instance=metric)
    return render(request ,'product/form.html', {
        'title': 'Delete Product',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })

@login_required
def category(request):
    categories = Category.objects.all()
    return render(request, 'product/category.html', {
        'title': 'Category',
        'categories': categories,
    })

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product category has been added.')
            return redirect('product:category')
    else:
        form = CategoryForm()
    return render(request, 'product/form.html', {
        'title': 'Add Category',
        'form': form,
    })

@login_required
def edit_category(request, category_primary_key):
    category = get_object_or_404(Category, id=category_primary_key)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product category has been edited.')
            return redirect('product:category')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'product/form.html', {
        'title': 'Edit Category', 
        'form': form,
    })

@login_required
def delete_category(request, category_primary_key):
    model = 'Category'
    is_delete = True
    category = get_object_or_404(Category, id=category_primary_key)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        category.delete()
        messages.success(request, 'Successful! Product category has been deleted.')
        return redirect('product:category')
    else:
        form = CategoryForm(instance=category)
    return render(request ,'product/form.html', {
        'title': 'Delete Category',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })

@login_required
def color(request):
    colors = Color.objects.all()
    return render(request, 'product/color.html', {
        'title': 'Colors',
        'colors': colors,
    })

@login_required
def add_color(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product color has been added.')
            return redirect('product:color')
    else:
        form = ColorForm()
    return render(request, 'product/form.html', {
        'title': 'Add Color',
        'form': form,
    })

@login_required
def edit_color(request, color_primary_key):
    color = get_object_or_404(Color, id=color_primary_key)
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=color)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product color has been edited.')
            return redirect('product:color')
    else:
        form = ColorForm(instance=color)
    
    return render(request, 'product/form.html', {
        'title': 'Edit Color', 
        'form': form,
    })

@login_required
def delete_color(request, color_primary_key):
    model = 'Color'
    is_delete = True
    color = get_object_or_404(Color, id=color_primary_key)
    if request.method == 'POST':
        form = ColorForm(request.POST, instance=color)
        color.delete()
        messages.success(request, 'Successful! Product color has been deleted.')
        return redirect('product:color')
    else:
        form = ColorForm(instance=color)
    return render(request ,'product/form.html', {
        'title': 'Delete Color',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })

@login_required
def size(request):
    sizes = Size.objects.all()
    return render(request, 'product/size.html', {
        'title': 'Sizes',
        'sizes': sizes,
    })

@login_required
def add_size(request):
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product size has been added.')
            return redirect('product:size')
    else:
        form = SizeForm()
    return render(request, 'product/form.html', {
        'title': 'Add Size',
        'form': form,
    })

@login_required
def edit_size(request, size_primary_key):
    size = get_object_or_404(Size, id=size_primary_key)
    if request.method == 'POST':
        form = SizeForm(request.POST, instance=size)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Product size has been edited.')
            return redirect('product:size')
    else:
        form = SizeForm(instance=size)
    
    return render(request, 'product/form.html', {
        'title': 'Edit Size', 
        'form': form,
    })

@login_required
def delete_size(request, size_primary_key):
    model = 'Size'
    is_delete = True
    size = get_object_or_404(Size, id=size_primary_key)
    if request.method == 'POST':
        form = SizeForm(request.POST, instance=size)
        size.delete()
        messages.success(request, 'Successful! Product size has been deleted.')
        return redirect('product:size')
    else:
        form = SizeForm(instance=size)
    return render(request ,'product/form.html', {
        'title': 'Delete Size',
        'form': form,
        'is_delete': is_delete,
        'model': model,
    })