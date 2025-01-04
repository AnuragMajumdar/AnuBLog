from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)

    class Meta:
        db_table = 'users_customuser'

    def __str__(self):
        return self.username

