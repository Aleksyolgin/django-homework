from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class CustomUser(AbstractUser):
#     pass

User = get_user_model()
