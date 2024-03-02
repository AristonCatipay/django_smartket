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
