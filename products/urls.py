from django.urls import path
from products import views
from django.contrib.auth import views as auth_views
from .views import search_results

urlpatterns = [
    path('login/', views.login_view, name='login'),  # ✅ Fixed Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('product-list/', views.product_list, name='product_list'),
    path('men/', views.men, name='men'),  # Fixed to match view function name
    path('women/', views.women, name='women'),  # Fixed to match view function name
    path('kids/', views.kids, name='kids'),  # Fixed to match view function name
    path('search/', search_results, name='search_results'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('', views.product_list, name='product_list'),
]
