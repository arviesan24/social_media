"""Serializers for Posts app."""

from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'url', 'owner', 'content', 'privacy', 'datetime_created',
            'datetime_modified')
