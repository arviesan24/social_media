"""Viewsets for Accounts app."""

from actstream.actions import follow
from actstream.actions import unfollow
from django.db.models import Q
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


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin user to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the admin users.
        return request.user.is_staff

class ProfileFilterSet(django_filters.FilterSet):
    """FilterSet for ProfileViewSet."""

    def get_multiple_fields(self, queryset, name, value):
        """Method for searching multiple fields."""
        return queryset.filter(
            Q(first_name__contains=value) |
            Q(last_name__contains=value) |
            Q(description__contains=value) |
            Q(user__username__contains=value) |
            Q(user__email__contains=value))

    multiple_fields = django_filters.CharFilter(method='get_multiple_fields')

    class Meta:
        model = models.Profile
        fields = ['user', 'id', 'first_name', 'last_name', 'multiple_fields']


class RelationshipFilterSet(django_filters.FilterSet):
    """FilterSet for RelationShipViewSet."""

    def get_receiver_multifield_search(self, queryset, name, value):
        """Method for searching multiple fields."""
        return queryset.filter(
            Q(receiver__first_name__contains=value) |
            Q(receiver__last_name__contains=value) |
            Q(receiver__profile__description__contains=value) |
            Q(receiver__username__contains=value) |
            Q(receiver__email__contains=value))

    receiver_multifield_search = django_filters.CharFilter(
        method='get_receiver_multifield_search')

    class Meta:
        model = models.Relationship
        fields = [
            'sender', 'receiver', 'request', 'type',
            'receiver_multifield_search']


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
    serializer_class = serializers.RelationshipSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsRequestSenderOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = RelationshipFilterSet


    def partial_update(self, request, *args, **kwargs):
        """Returns `patched` Relationship instance."""
        response = super().partial_update(request, *args, **kwargs)
        # check if request contains `request` field and was set to `confirmed`.
        if (request.data['request'] and
                self.get_object().request.status == 'confirmed'):
            # make the friend request sender follow the receiver.
            follow(request.user, self.get_object().receiver)
            # make the friend request receiver follow the sender.
            follow(self.get_object().receiver, request.user)

        return response

    def destroy(self, request, *args, **kwargs):
        """Deletes `Relationship` instance."""
        # make the friend request sender unfollow the receiver.
        unfollow(request.user, self.get_object().receiver)
        # make the friend request receiver unfollow the sender.
        unfollow(self.get_object().receiver, request.user)

        return super().destroy(request, *args, **kwargs)


class RequestViewSet(viewsets.ModelViewSet):
    """Viewset for RequestSerializer"""

    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsAdminOrReadOnly,)


class RelationshipTypeViewSet(viewsets.ModelViewSet):
    """Viewset for RelationshipTypeSerializer"""

    queryset = models.RelationshipType.objects.all()
    serializer_class = serializers.RelationshipTypeSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsAdminOrReadOnly,)
