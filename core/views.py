from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html', {
        'title': 'Welcome',
    })

def signup(request):
    return render(request, 'core/signup.html', {
        'title': 'Signup',
    })
