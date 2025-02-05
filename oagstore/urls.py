# oag_store/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),
    
    # Main store app URLs (home, login, register, product details)
    path('', include('products.urls')),  # Include the URLs from the 'products' app
]