from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    logo = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    title_art = models.CharField(max_length=60)
    author_art = models.CharField(max_length=30)
    summary_art = models.CharField(max_length=200)
