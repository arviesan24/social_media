"""Viewsets for Accounts app."""

from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow account owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow profile owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class IsRequestSenderOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow request sender to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the sender of the snippet.
        return obj.sender == request.user


class ProfileFilterSet(django_filters.FilterSet):
    """FilterSet for ProfileViewSet."""

    class Meta:
        model = models.Profile
        fields = ['user', 'first_name', 'last_name']

class RelationShipFilterSet(django_filters.FilterSet):
    """FilterSet for RelationShipViewSet."""

    class Meta:
        models = models.Relationship
        fields = ['sender__id', 'receiver__id', 'request__status', 'type']


class UserViewSet(viewsets.ModelViewSet):
    """Viewset for UserSerializer"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class ProfileViewSet(viewsets.ModelViewSet):
    """Viewset for ProfileSerializer"""

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsProfileOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = ProfileFilterSet


class RelationshipViewSet(viewsets.ModelViewSet):
    """Viewset for RelationshipSerializer"""

    queryset = models.Relationship.objects.all()
    serializers_class = serializers.RelationshipSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsRequestSenderOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = RelationShipFilterSet
