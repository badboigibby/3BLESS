# products/models.py

from django.db import models
from django.contrib.auth import get_user_model

# Get the User model dynamically
User = get_user_model()

# Category Model: Store product categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product Model: Store product details
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Add stock field
    created_at = models.DateTimeField(auto_now_add=True)  # Add created_at field
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True)  # Add description field
    image_url = models.URLField(blank=True, null=True)  # Add image_url field

    def __str__(self):
        return self.name

# CartItem Model: Store items in the user's shopping cart
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

# Review model to store reviews for products
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted the review
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')  # Product being reviewed
    rating = models.IntegerField()  # Rating given to the product (e.g., 1-5)
    comment = models.TextField()  # Text comment of the review
    created_at = models.DateTimeField(auto_now_add=True)  # Add created_at field

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'