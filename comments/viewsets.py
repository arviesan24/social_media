"""Viewsets for Comments app."""

from rest_framework import viewsets

from . import serializers
from . import models

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer