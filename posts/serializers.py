from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class PostsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True, read_only=True)
    creationd = serializers.DateTimeField(format="%d/%m/%y %H:%M")

    class Meta:
        model = Post
        fields = "__all__"
