from .models import Category, Product
from django.contrib import admin

# Register models to appear in the admin interface
admin.site.register(Category)
admin.site.register(Product)