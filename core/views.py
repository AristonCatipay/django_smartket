from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html', {
        'title': 'Welcome',
    })

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken.')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken.')
                return redirect('core:signup')
            else:
                # Create the user.
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                # Log the user using the credentials.
                user_credentials = auth.authenticate(username=username, password=password)
                auth.login(request, user_credentials)

                return redirect('core:index')
        else: 
            messages.info(request, 'Passwords don\'t match')
            return redirect('core:signup')
    else: 
        return render(request, 'core/signup.html', {
            'title': 'Signup',
        })
