from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('farmer','Farmer'),
        ('provider','Service Provider'),

        ('warehouse_owner','Warehouse Owner')
    )

    role = models.CharField(max_length=50,choices = ROLES)
    phone_number = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.username
# Create your models here.
