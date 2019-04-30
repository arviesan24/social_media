"""Serializers for Accounts app."""
from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'url', 'username', 'email', 'active',
            'datetime_created', 'datetime_modified')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Profile
        fields = (
            'url', 'user', 'first_name', 'last_name', 'gender', 'preference',
            'birth_date', 'phone_number', 'address', 'description',
            'datetime_created', 'datetime_modified')


class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Relationship
        fields = (
            'sender', 'receiver', 'type', 'datetime_created',
            'datetime_modified')
