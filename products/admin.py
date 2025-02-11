from django.contrib import admin
from .models import Category, Product, Review  # Correct import

# CategoryAdmin: Control how the Category model appears in the admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display ID and Name
    search_fields = ('name',)  # Enable search by category name
    ordering = ('name',)  # Display categories in alphabetical order

# ProductAdmin: Control how the Product model appears in the admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')  # Fields to display
    list_filter = ('category', 'price')  # Filters by category and price
    search_fields = ('name', 'category__name')  # Enable searching by product name and category name
    ordering = ('-price',)  # Display products ordered by price
    list_editable = ('price',)  # Allow price editing from the list view
    list_per_page = 20  # Limit products per page

# ReviewAdmin: Control how the Review model appears in the admin panel
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')  # Display user, product, rating, and creation date
    list_filter = ('rating', 'created_at')  # Filter by rating and creation date
    search_fields = ('user__username', 'product__name')  # Enable searching by username and product name
    ordering = ('-created_at',)  # Display newest reviews first
