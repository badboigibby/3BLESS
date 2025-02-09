from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Product, Review, CartItem
from .forms import UserRegistrationForm, ReviewForm

# Home view displaying all products
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Product list view displaying all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Product detail view to display product and reviews
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    review_form = ReviewForm(request.POST or None)

    if request.method == 'POST' and review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = request.user
        review.product = product
        review.save()
        return redirect('product_detail', product_id=product.id)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
    })

# Add to Cart View
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

# Update Cart View
@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity'))
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
        except ValueError:
            pass  # Prevent crashes if input is invalid
    return redirect('cart')

# Remove from Cart View
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

# Cart View
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Checkout View
@login_required
def checkout(request):
    if request.method == 'POST':
        send_mail(
            'Order Confirmation',
            'Thank you for your order!',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=True,
        )
        return redirect('order_confirmation')
    return render(request, 'checkout.html')

# Order Confirmation View
@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')

# Search View
def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {'results': results, 'query': query})

# Men Category View
def men(request):
    products = Product.objects.filter(category='Men')
    return render(request, 'men.html', {'products': products})

# Women Category View
def women(request):
    products = Product.objects.filter(category='Women')
    return render(request, 'women.html', {'products': products})

# Kids Category View
def kids(request):
    products = Product.objects.filter(category='Kids')
    return render(request, 'kids.html', {'products': products})

# Category Views
def men_category(request):
    products = Product.objects.filter(category__name='Men')
    return render(request, 'products/product_list.html', {'products': products})

def women_category(request):
    products = Product.objects.filter(category__name='Women')
    return render(request, 'products/product_list.html', {'products': products})

def kids_category(request):
    products = Product.objects.filter(category__name='Kids')
    return render(request, 'products/product_list.html', {'products': products})

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# Additional Pages
def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')

def reviews(request):
    return render(request, 'reviews.html')

# View to list all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'oagstore/product_list.html', {'products': products})

# View to display product details
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'oagstore/product_detail.html', {'product': product})