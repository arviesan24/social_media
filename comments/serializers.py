"""Serializers for Comments app."""

import json

from django.contrib.contenttypes.models import ContentType
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
            return value.__class__.__name__
        raise Exception('Unexpected type of commented object')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Comment model."""

    content_object = ContentObjectRelatedField(queryset=Comment.objects.all())
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'url', 'owner', 'object_id', 'content_object', 'content',
            'children', 'is_parent', 'datetime_created', 'datetime_modified')

    def get_children(self, obj):
        """Return `children` serialized objects."""
        data = dj_serializers.serialize('json', obj.children())
        # change `data` string to json
        json_data = json.loads(data)
        return json_data
