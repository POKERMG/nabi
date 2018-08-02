from django.contrib.auth.models import AbstractUser
from django.db import models


# Extend User Class AbstractUser
class User(AbstractUser):
    created_by = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
