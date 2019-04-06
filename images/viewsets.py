"""Viewsets for Comments app."""
from django.contrib.contenttypes.models import ContentType
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models


class IsAlbumOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow object owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsImageOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow album owner to edit image.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.album.owner == request.user


class ImageFilterSet(django_filters.FilterSet):
    """FilterSet for ImageViewSet."""

    class Meta:
        model = models.Image
        fields = ['album__owner__id',]


class ImageViewSet(viewsets.ModelViewSet):
    """Viewset for CommentSerializer."""

    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = (permissions.IsAuthenticated, IsImageOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = ImageFilterSet


class AlbumViewSet(viewsets.ModelViewSet):
    """Viewset for CommentSerializer."""

    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, IsAlbumOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    # filterset_class = CommentFilterSet
