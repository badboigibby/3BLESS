# products/admin.py

from django.contrib import admin
from .models import Category, Product, Review, CartItem

# CategoryAdmin: Control how the Category model appears in the admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display ID and Name
    search_fields = ('name',)  # Enable search by category name
    ordering = ('name',)  # Display categories in alphabetical order

# ProductAdmin: Control how the Product model appears in the admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'created_at')  # Control which fields are displayed
    list_filter = ('category', 'created_at', 'price')  # Filters by category, date, and price
    search_fields = ('name', 'category__name')  # Enable searching by product name and category name
    ordering = ('-created_at',)  # Display newest products first
    list_editable = ('price', 'stock')  # Allow price and stock editing from the list view
    list_per_page = 20  # Control how many products are displayed per page

# ReviewAdmin: Control how the Review model appears in the admin panel
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')  # Display user, product, rating, and creation date
    list_filter = ('rating', 'created_at')  # Filter by rating and creation date
    search_fields = ('user__username', 'product__name')  # Enable searching by username and product name
    ordering = ('-created_at',)  # Display newest reviews first

# CartItemAdmin: Control how the CartItem model appears in the admin panel
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_price')  # Display user, product, quantity, and total price
    list_filter = ('user', 'product')  # Filter by user and product
    search_fields = ('user__username', 'product__name')  # Enable searching by username and product name
    ordering = ('-id',)  # Display newest cart items first

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_quantity')
    search_fields = ('name', 'category')
    list_filter = ('category',)