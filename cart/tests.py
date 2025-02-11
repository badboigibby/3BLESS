# cart/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product
from .models import CartItem

User = get_user_model()

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)

    def test_total_price(self):
        self.assertEqual(self.cart_item.total_price, 20.00)
