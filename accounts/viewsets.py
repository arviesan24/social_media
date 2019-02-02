"""Viewsets for Accounts app."""

from rest_framework import viewsets

from . import serializers
from . import models

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
