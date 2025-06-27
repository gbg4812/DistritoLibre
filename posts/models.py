from django.db import models

from postsauth.models import DistritoLibreUser

# Create your models here.


def get_anonymus_user():
    return DistritoLibreUser.objects.get_or_create(username="anonymus")[0]


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)


class TagBuilding(Tag):
    icon = models.CharField(max_length=128, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(
        DistritoLibreUser, on_delete=models.CASCADE, default=get_anonymus_user
    )
    creationd = models.DateTimeField(auto_now_add=True)
    lastmodif = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag)

    description = models.TextField(max_length=400, blank=True)
    content = models.TextField(max_length=2000, blank=True)
    icon = models.CharField(max_length=128, blank=True)
