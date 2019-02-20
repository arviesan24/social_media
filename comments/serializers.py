"""Serializers for Comments app."""

from django.core import serializers as dj_serializers
from django.http import HttpResponse

from rest_framework import serializers

from .models import Comment

from posts.models import Post


class ContentObjectRelatedField(serializers.RelatedField):
    """A custom field to use for the `content_object` generic relationship."""

    def to_representation(self, value):
        """Serialize content objects to a class name representation."""
        if isinstance(value, Comment):
            return value.__class__.__name__
        if isinstance(value, Post):
            print(value)
            return value.__class__.__name__
        raise Exception('Unexpected type of commented object')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Comment model."""

    content_object = ContentObjectRelatedField(queryset=Comment.objects.all())

    class Meta:
        model = Comment
        fields = (
            'url', 'owner', 'object_id', 'content_object', 'content',
            'datetime_created', 'datetime_modified')
