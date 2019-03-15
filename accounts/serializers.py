"""Serializers for Accounts app."""
from django.utils import timesince
from rest_framework import serializers

from .models import Profile
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url', 'username', 'email', 'active',
            'datetime_created', 'datetime_modified')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'url', 'user', 'first_name', 'last_name', 'gender', 'preference',
            'birth_date', 'phone_number', 'address', 'description',
            'datetime_created', 'datetime_modified')
