from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=50, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)    # Add any additional fields you want

    def __str__(self):
        return self.username
