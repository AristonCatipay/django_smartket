from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'user_profile/index.html', {
        'title': 'Profile',
    })

