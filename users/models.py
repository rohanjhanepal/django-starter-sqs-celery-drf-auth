from typing import Iterable
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.CharField(max_length=250, unique=True, null=True, blank=True)
    deviceID = models.CharField(max_length=250, unique=True, null=True, blank=True)
    # password = models.
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    user_date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    # objects = UserManager()
    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
        ('deviceID', 'deviceID'),
    ]
    registration_method = models.CharField(
        max_length=10,
        choices=REGISTRATION_CHOICES,
        default='deviceID'
    )

    def __str__(self):
       return self.username
    


    

