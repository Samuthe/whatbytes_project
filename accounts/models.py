from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

"""@package docstring
This module contains the CustomUser model, fields and methods to create a custom User model in Django."""
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    """CustomUser model fields and methods. Inherits from AbstractUser model."""
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True
    )

    def __str__(self):
        return self.username
