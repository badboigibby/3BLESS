from django.urls import path
from . import views  # Import views from the current app
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # View product details
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add a product to the cart
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),  # Update cart item quantity
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove item from cart
    path('cart/', views.cart, name='cart'),  # View cart contents
    path('checkout/', views.checkout, name='checkout'),  # Checkout process
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),  # Order confirmation page
    path('product-list/', views.product_list, name='product-list'),  # List of products
    path('men/', views.men_category, name='men'),  # Men category
    path('women/', views.women_category, name='women'),  # Women category
    path('kids/', views.kids_category, name='kids'),  # Kids category
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),  # ADD THIS LINE
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('terms/', views.terms, name='terms'),  # Ensure this exists
    path('contact/', views.contact, name='contact')

]
