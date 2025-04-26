from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class PostsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = "__all__"
