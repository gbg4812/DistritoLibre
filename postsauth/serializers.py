from rest_framework import serializers

from postsauth.models import DistritoLibreUser


class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = DistritoLibreUser
        fields = ["username", "password", "email"]
