from django.shortcuts import render

def index(request):
    return render(request, 'number/index.html', {
        'title': 'Customer Number'
    })