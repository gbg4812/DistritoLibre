from django.db import models
from django.contrib.auth.models import User


class DistritoLibreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_code = models.CharField(max_length=6)


# Create your models here.
