# products/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import terms_view
from django.urls import path, include
from django.contrib import admin
from .views import reviews  # Import the reviews view
from .views import search


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('', views.home, name='home'),
    path('men/', views.men, name='men'),  # Ensure this exists
    path('women/', views.women, name='women'),
    path('kids/', views.kids, name='kids'),
    path('terms/', terms_view, name='terms'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('kids/', views.kids, name='kids'),
    path('terms/', views.terms, name='terms'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', reviews, name='reviews'),
    path('search/', views.search, name='search'),
    path('terms/', terms_view, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)