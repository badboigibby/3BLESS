# user/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class UserAppTests(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        # Check that a Profile was created for the new user
        self.assertIsNotNone(user.profile)
