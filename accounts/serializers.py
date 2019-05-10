"""Serializers for Accounts app."""
from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = models.User
        fields = (
            'url', 'username', 'email', 'active',
            'datetime_created', 'datetime_modified')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Profile model."""

    user_id = serializers.SerializerMethodField()
    class Meta:
        model = models.Profile
        fields = (
            'url', 'id', 'user', 'user_id', 'first_name', 'last_name', 'gender',
            'preference', 'birth_date', 'phone_number', 'address',
            'description', 'slug', 'datetime_created', 'datetime_modified')

    def get_user_id(self, obj):
        """Returns user id of Profile owner."""
        return obj.user.id



class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Relationship model."""

    class Meta:
        model = models.Relationship
        fields = (
            'url', 'sender', 'receiver', 'request', 'type',
            'datetime_created', 'datetime_modified')


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Request model."""

    class Meta:
        model = models.Request
        fields = (
            'url', 'status',
            'datetime_created', 'datetime_modified')


class RelationshipTypeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for RelationshipType model."""

    class Meta:
        model = models.RelationshipType
        fields = (
            'url', 'name',
            'datetime_created', 'datetime_modified')
