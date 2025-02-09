# products/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('product-list/', views.product_list, name='product_list'),
    path('men/', views.men_category, name='men'),
    path('women/', views.women_category, name='women'),
    path('kids/', views.kids_category, name='kids'),
    path('search/', views.search, name='search'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]
