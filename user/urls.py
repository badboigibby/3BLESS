# user/urls.py
from django.urls import path
from . import views

app_name = 'user'  # This is necessary to support the namespace in the include()

# URL patterns for user-related views
urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for login page
    path('register/', views.register_view, name='register'),  # URL for register page
    # Add other URLs here if needed
]
