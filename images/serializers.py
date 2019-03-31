"""Serializers for Images app."""

from rest_framework import serializers

from . import models


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Image model."""

    class Meta:
        model = models.Image
        fields = (
            'url', 'id', 'location', 'album', 'privacy', 'datetime_created',
            'datetime_modified')
