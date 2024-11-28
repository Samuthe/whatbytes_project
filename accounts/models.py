from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

"""This is the custom user model that extends the AbstractUser model provided by Django.
It adds additional fields to the user model such as image, age, bio, location, website, and social media links.
It also adds the groups and user_permissions fields to the user model."""
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

    """The groups and user_permissions fields are ManyToManyFields that relate to the Group and Permission models provided by Django.
    This allows users to be assigned to groups and given specific permissions."""
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
