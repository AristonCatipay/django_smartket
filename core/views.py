from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .decorators import unauthenticated_user
from user_profile.models import Profile
from product.models import Product, Category, Color, Size, Metric_Unit
from customer.models import Customer
from credit.models import Credit_Transaction

@unauthenticated_user
def home(request):
    return render(request, 'core/home.html', {
        'title': 'Home',
    })

def index(request):
    product_total = Product.objects.count()
    category_total = Category.objects.count()
    color_total = Color.objects.count()
    size_total =  Size.objects.count()
    metric_unit_total = Metric_Unit.objects.count()
    customer_total = Customer.objects.count()
    credit_transaction_total = Credit_Transaction.objects.count()
    credit_transaction_not_paid_total = Credit_Transaction.objects.filter(is_paid=False).count()
    return render(request, 'core/index.html', {
        'title': 'Welcome',
        'product_total': product_total,
        'category_total': category_total,
        'color_total': color_total,
        'size_total': size_total,
        'metric_unit_total': metric_unit_total,
        'customer_total': customer_total,
        'credit_transaction_total': credit_transaction_total,
        'credit_transaction_not_paid_total': credit_transaction_not_paid_total,
    })

@unauthenticated_user
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
                messages.error(request, 'Email is already taken.')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('core:signup')
            else:
                # Create the user.
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                # Log the user using the credentials.
                credentials = auth.authenticate(username=username, password=password)
                auth.login(request, credentials)
                # Create user profile.
                user = User.objects.get(username=username)
                profile = Profile.objects.create(user=user)
                profile.save()
                
                messages.success(request, 'Account created successfully! Welcome to our community.')
                return redirect('core:index')
        else: 
            messages.error(request, 'Passwords don\'t match')
            return redirect('core:signup')
    else: 
        return render(request, 'core/signup.html', {
            'title': 'Signup',
        })

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if  user is not None:
            # A backend authenticate the credentials.
            auth.login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('core:index')
        else: 
            # No backend authenticated the credentails.
            messages.error(request, 'Invalid credentials. Please check your username and password.')
            return redirect('core:signin')
    else:
        return render(request, 'core/signin.html', {
            'title': 'Sign in'
        })

def signout(request):
    auth.logout(request)
    messages.success(request, 'Logout successful. Have a great day!')
    return redirect('core:signin')