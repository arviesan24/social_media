"""Serializers for Comments app."""

from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'url', 'owner', 'post', 'content', 'datetime_created',
            'datetime_modified')
