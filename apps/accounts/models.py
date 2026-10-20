from django.contrib.auth.models import AbstractUser
from django.db import models

# TODO: Add custom fields to the User model to represent info about the user, such as profile picture, bio, etc.
class User(AbstractUser):
    pass
