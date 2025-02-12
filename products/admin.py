from django.contrib import admin
from .models import Category, Product, Review  # Import models


# CategoryAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # ✅ No 'price' (Categories don't have prices)
    search_fields = ('name',)  # ✅ Corrected search field
    ordering = ('name',)  # ✅ Must be a tuple
    list_filter = ('name',)  # ✅ Filtering categories by name

# ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # ✅ Only valid fields
    list_filter = ('price',)  # ✅ Removed 'category' if it's not a field in Product
    search_fields = ('name', 'category__name')  # ✅ Searching by product name and category name
    ordering = ('-price',)  # ✅ Ordering by price descending
    list_editable = ('price',)  # ✅ Allow price editing from list view
    list_per_page = 20  # ✅ Limit products per page

# ReviewAdmin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')  # ✅ Display user, product, rating, and created_at
    list_filter = ('rating', 'created_at')  # ✅ Filtering by rating and created_at
    search_fields = ('user__username', 'product__name')  # ✅ Searching by user and product name
    ordering = ('-created_at',)  # ✅ Ordering reviews from newest to oldest
