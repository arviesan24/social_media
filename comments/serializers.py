"""Serializers for Comments app."""

import json

from django.contrib.contenttypes.models import ContentType
from django.core import serializers as dj_serializers
from django.http import HttpResponse
from django.utils import timesince

from datetime import datetime
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
    date_to_display = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'url', 'id', 'owner', 'content_type', 'object_id', 'parent',
            'is_parent', 'content', 'children', 'datetime_created',
            'datetime_modified', 'date_to_display')

    def get_children(self, obj):
        """Return `children` serialized objects."""
        data = dj_serializers.serialize('json', obj.children())
        # change `data` string to json
        json_data = json.loads(data)
        return json_data

    def get_date_to_display(self, obj):
        """Return timesince formatted date."""

        # returns datetime created
        if timesince.timesince(obj.datetime_created) == (
                timesince.timesince(obj.datetime_modified)):
            created_value = timesince.timesince(obj.datetime_created)
            comment_string = 'Replied'
            if obj.is_parent:
                comment_string = 'Commented'

            return f'{comment_string} {created_value} ago'
        
        #returns datetime modified
        modified_value = timesince.timesince(obj.datetime_modified)
        return f'Edited {modified_value} ago'
