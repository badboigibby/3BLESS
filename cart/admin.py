from django.contrib import admin
from .models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'created_at']  # Remove 'updated_at' if it doesn't exist
    search_fields = ['product__name']  

admin.site.register(CartItem, CartItemAdmin)
