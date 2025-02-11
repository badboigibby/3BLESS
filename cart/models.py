from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.utils.timezone import now  # Import timezone for default value

# Get the User model dynamically
User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when modified

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (User: {self.user.username})"

    def total_price(self):
        """Calculate total price for this cart item"""
        return self.quantity * self.product.price

    class Meta:
        ordering = ['-created_at']  # Orders by newest items first
        verbose_name_plural = "Cart Items"  # Corrects display name in Django admin
