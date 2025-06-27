from rest_framework import serializers

from postsauth.models import User


class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
