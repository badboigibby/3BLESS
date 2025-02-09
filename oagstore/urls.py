from django.contrib import admin
from django.urls import path, include
from products import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='home'),  # Home page
    path('men/', views.men, name='men'),  # Men category
    path('women/', views.women, name='women'),  # Women category
    path('kids/', views.kids, name='kids'),  # Kids category
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line if missing
    path('contact/', include('products.urls')),  # If 'contact' is in another app
    path('', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),  # Example for listing products
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Example for product detail page
    # Add other URL patterns here
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oagstore.urls')),  # Assuming your app is named oagstore, replace with 'product' if needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
