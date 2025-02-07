from django.contrib import admin
from django.urls import path, include
from products import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='home'),  # Home page
    path('men/', views.men, name='men'),  # Men category
    path('women/', views.women, name='women'),  # Women category
    path('kids/', views.kids, name='kids'),  # Kids category
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line if missing
    path('contact/', include('products.urls')),  # If 'contact' is in another app
    path('', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # Add other URL patterns here
]
