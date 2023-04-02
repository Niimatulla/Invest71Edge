from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    address = models.CharField(max_length=200)
    phone = models.PositiveIntegerField(default=+234)
    wallet = models.CharField(max_length=300, verbose_name="TRC 20 wallet address")
    approve = models.BooleanField(default=False)
    asset1 = models.BooleanField(default=False)
    asset2 = models.BooleanField(default=False)
    asset3 = models.BooleanField(default=False)
    asset4 = models.BooleanField(default=False)
