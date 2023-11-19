from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'user_profile/index.html', {
        'title': 'Profile',
    })

@login_required
def edit(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        image = request.FILES.get('image')

        profile = request.user.profile

        if image:
            profile.image = image

        # Update profile model
        profile.save()

        # Update user model
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.username = username
        request.user.email = email
        request.user.save()

        return redirect('profile:edit')

    return render(request, 'user_profile/edit.html', {
        'title': 'Edit Profile',
    })