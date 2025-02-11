from django.db import models
from django.contrib.auth.models import User  # Using the default User model

# Category model for products
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Product model related to Category
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=1)  # Default category with ID=1
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.stock


# CartItem model referencing the default User model and Product
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Using the default User model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name} for {self.user.username}'


# Review model referencing the User model and Product
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Using the default User model
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating out of 5
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'
