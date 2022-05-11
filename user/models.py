from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class UserProfile(AbstractUser):
    username = models.CharField(max_length=50, unique=True,
                                help_text="50 ta belgidan kup bulmasin"
                                )
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    @property
    def age(self):
        return date.today().year - self.birthday.year


