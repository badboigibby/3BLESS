# products/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import Product, Review
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from . import views
from .forms import ReviewForm
from .models import Review
from .models import Product

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to homepage after logout

# Home View (For homepage)
def home(request):
    return render(request, 'home.html')  # Render the home page template

# Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Categories Views
def men(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')

def kids(request):
    return render(request, 'kids.html')

# Terms and Reviews
def terms_view(request):
    return render(request, 'terms.html')

def terms(request):
    return render(request, 'products/terms.html')

def reviews(request):
    return render(request, 'products/reviews.html')

def reviews(request):
    if request.method == 'POST':
        name = request.POST['name']
        review = request.POST['review']
        Review.objects.create(name=name, review=review)
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            f'New Contact Form Submission from {name}',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.EMAIL_HOST_USER,  # From email
            [settings.EMAIL_HOST_USER],  # To email (your email)
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})  # Show success message
    return render(request, 'contact.html')

def reviews(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review = request.POST.get('review')
        Review.objects.create(name=name, review=review)  # Save the review
        return redirect('reviews')  # Redirect to the reviews page
    reviews = Review.objects.all().order_by('-created_at')  # Get all reviews
    return render(request, 'reviews.html', {'reviews': reviews})

def search(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Search for products by name, category, or description
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(category__icontains=query) | 
            Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()  # Show all products if no query
    return render(request, 'search.html', {'products': products, 'query': query})
