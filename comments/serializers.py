"""Serializers for Comments app."""

import json

from django.contrib.contenttypes.models import ContentType
from django.core import serializers as dj_serializers
from django.http import HttpResponse
from django.utils import timesince

from rest_framework import serializers

from .models import Comment

from posts.models import Post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Comment model."""

    # Reference link: https://stackoverflow.com/questions/24970610/
    # set-contenttype-by-name-in-generic-relation-in-django-rest-framework
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(), slug_field='model')
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'url', 'owner', 'content_type', 'object_id', 'parent', 'content',
            'children', 'is_parent', 'datetime_created', 'datetime_modified')

    def get_children(self, obj):
        """Return `children` serialized objects."""
        data = dj_serializers.serialize('json', obj.children())
        # change `data` string to json
        json_data = json.loads(data)
        return json_data
