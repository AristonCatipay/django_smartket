from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import RegionForm, ProvinceForm, CityMunicipalityForm, BarangayForm
from .models import Region, Province, City_Municipality, Barangay

@login_required
def view_region(request):
    query = request.GET.get('query', '')
    regions = Region.objects.all()

    if query:
        regions = regions.filter(Q(name__icontains=query) | Q(region_code__icontains=query) | Q(psgc_code__icontains=query))
    return render(request, 'address/region.html', {
        'title': 'Region',
        'regions': regions,
    })

@login_required
def create_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Region has been saved.')
    else:
        form = RegionForm()
    
    return render(request, 'address/form.html', {
        'title': 'Create New Region',
        'form': form,
    })

@login_required
def update_region(request, primary_key):
    region = get_object_or_404(Region, id = primary_key)

    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Region has been updated.')
    else: 
        form = RegionForm(instance=region)

    return render(request, 'address/form.html', {
        'title': 'Edit Region',
        'form': form,
    })

@login_required
def delete_region(request, region_primary_key):
    region = get_object_or_404(Region, pk=region_primary_key)
    region.delete()
    messages.success(request, 'Success! The region has been successfully deleted!')
    return redirect('region:view_region')

@login_required
def view_province(request):
    query = request.GET.get('query', '')
    provinces = Province.objects.all()

    if query:
        provinces = provinces.filter(Q(name__icontains=query) | Q(province_code__icontains=query) | Q(psgc_code__icontains=query))
    return render(request, 'address/province.html', {
        'title': 'Province',
        'provinces': provinces,
    })

@login_required
def create_province(request):
    if request.method == 'POST':
        form = ProvinceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Province has been saved.')
    else:
        form = ProvinceForm()
    
    return render(request, 'address/form.html', {
        'title': 'Create New Province',
        'form': form,
    })

@login_required
def update_province(request, primary_key):
    province = get_object_or_404(Province, id = primary_key)

    if request.method == 'POST':
        form = ProvinceForm(request.POST, instance=province)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successful! Province has been updated.')
    else: 
        form = ProvinceForm(instance=province)

    return render(request, 'address/form.html', {
        'title': 'Edit Province',
        'form': form,
    })

@login_required
def delete_province(request, province_primary_key):
    province = get_object_or_404(Province, pk=province_primary_key)
    province.delete()
    messages.success(request, 'Success! The province has been successfully deleted!')
    return redirect('address:view_province')

@login_required
def view_city_municipality(request):
    query = request.GET.get('query', '')
    city_or_municipalities = City_Municipality.objects.all()

    if query:
        city_or_municipalities = city_or_municipalities.filter(Q(name__icontains=query) | Q(city_municipality_code__icontains=query) | Q(psgc_code__icontains=query))
    return render(request, 'address/city_municipality.html', {
        'title': 'Province',
        'city_or_municipalities': city_or_municipalities,
    })