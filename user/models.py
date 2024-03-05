from django.db import models
from uuid import uuid4

# Create your models here.

class User(models.Model):

    uid = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
