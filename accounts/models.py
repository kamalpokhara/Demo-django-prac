from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.
GENDER_CHOICES= [
    ('M', 'Male'),
    ('F', 'FeMale'),
    ('O', 'other'),
]

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ['email', 
                       'phone', 'gender']

    def __str__(self):
        return self.username