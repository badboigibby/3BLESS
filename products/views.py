from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Product, Review, CartItem  # Import necessary models
from .forms import UserRegistrationForm, ReviewForm
# Removed unused import for SomeModel, assuming it's no longer required

# Home view displaying all products
def home(request):
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'home.html', {'products': products})

# Product list view displaying all products
def product_list(request):
    products = Product.objects.all()  # Get all products from the database
    return render(request, 'products/product_list.html', {'products': products})

# Product detail view to display product and reviews
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)  # Get reviews for the product
    review_form = ReviewForm(request.POST or None)  # Form to submit a review

    # Handle the review form submission
    if request.method == 'POST' and review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = request.user  # Associate review with the current user
        review.product = product  # Associate review with the product
        review.save()  # Save the review to the database
        return redirect('product_detail', product_id=product.id)  # Redirect to the same page to see the new review

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
            pass  # Prevents crashes if input is invalid
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
        # Example: Send confirmation email (optional)
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

def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'products/search_results.html', {'results': results, 'query': query})

# views.py
from django.shortcuts import render
from .models import Product

def men_category(request):
    products = Product.objects.filter(category__name='Men')
    return render(request, 'products/product_list.html', {'products': products})

def women_category(request):
    products = Product.objects.filter(category__name='Women')
    return render(request, 'products/product_list.html', {'products': products})

def kids_category(request):
    products = Product.objects.filter(category__name='Kids')
    return render(request, 'products/product_list.html', {'products': products})

# products/views.py

def men(request):
    # Fetch products for the "Men" category
    products = Product.objects.filter(category='Men')
    return render(request, 'men.html', {'products': products})

def women(request):
    # Fetch products for the "Women" category
    products = Product.objects.filter(category='Women')
    return render(request, 'women.html', {'products': products})

def kids(request):
    # Fetch products for the "Kids" category
    products = Product.objects.filter(category='Kids')
    return render(request, 'kids.html', {'products': products})

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')  # Ensure 'contact.html' exists

def reviews(request):
    return render(request, 'reviews.html')  # Ensure this template exists

def register(request):
    return render(request, 'register.html')

def register(request):
    return render(request, 'login.html')