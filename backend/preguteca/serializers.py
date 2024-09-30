from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "logo",
            "author",
            "title_art",
            "author_art",
            "summary_art",
        ]
