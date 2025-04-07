from django.forms import CharField
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class PostsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ["id", "title", "author", "section", "content", "coverimg"]
