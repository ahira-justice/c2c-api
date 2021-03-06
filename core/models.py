from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from uuid import uuid4 as uid

from core.managers import UserManager
from utils.states import STATE_CHOICES


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    """User profile model to extend user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    state_of_residence = models.CharField(max_length=2, choices=STATE_CHOICES)

    def __str__(self):
        return self.user.email


class Buyer(models.Model):
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    """Model for representing classified item"""
    id = models.UUIDField(primary_key=True, default=uid, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    url = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, blank=True)

    def __str__(self):
        return self.name
