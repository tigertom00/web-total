from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    phone = models.IntegerField(default=0)
    profile_picture = models.ImageField(
        upload_to='profile_image', default='default/profile.png')

    def __str__(self):
        return self.username
