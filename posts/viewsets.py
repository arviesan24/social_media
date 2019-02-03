"""Viewsets for Posts app."""

from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
