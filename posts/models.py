from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def get_anonymus_user():
    return User.objects.get_or_create(username="anonymus")[0]


class Tag(models.Model):
    name = models.CharField(max_length=64, primary_key=True)


class Post(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=get_anonymus_user
    )

    tags = models.ManyToManyField(Tag)

    content = models.CharField(max_length=1000, blank=True)
    icon = models.URLField(blank=True)
