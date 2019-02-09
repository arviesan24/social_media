"""Serializers for Comments app."""

from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Comment model."""

    class Meta:
        model = Comment
        fields = (
            'url', 'owner', 'object_id', 'content_object', 'content',
            'datetime_created', 'datetime_modified')
