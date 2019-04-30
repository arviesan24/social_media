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
            'url', 'sender', 'receiver', 'request', 'type',
            'datetime_created', 'datetime_modified')


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Request
        fields = (
            'url', 'status',
            'datetime_created', 'datetime_modified')
