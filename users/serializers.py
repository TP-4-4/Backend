from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
