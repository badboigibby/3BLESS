# oagstore/views.py

from django.shortcuts import render

# You can add other views as needed for your project. Here's another example:
def about(request):
    return render(request, 'about.html')  # Make sure you have an 'about.html' template

# Example for a contact page that receives data from a form
def contact(request):
    if request.method == 'POST':
        # Handle the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You could save this data or send an email here
    return render(request, 'contact.html')  # Make sure you have a 'contact.html' template

# oagstore/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Cart URLs
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),

    # Checkout and Order Confirmation
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),

    # Product list page
    path('products/', views.product_list, name='product_list'),
]
