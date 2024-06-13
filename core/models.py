from django.db import models
from django.contrib.auth.models import AbstractUser
    
class usuarios(AbstractUser):
    email = models.EmailField(unique=True)
    last_name2 = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.username + " - " + self.area.nombre