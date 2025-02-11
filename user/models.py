from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use the correct user model
    bio = models.TextField()  # Field exists to match the form
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Optional field

    def __str__(self):
        return self.user.username

# Signal to automatically create or update the user profile when a User is created or updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # Use the correct user model reference
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
