"""Viewsets for Comments app."""
from django.contrib.contenttypes.models import ContentType
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models


class IsOwnerOrReadOnly(permissions.BasePermission):
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


class CommentFilterSet(django_filters.FilterSet):
    """FilterSet for CommentViewSet."""

    def get_content_type():
        """Return list for `content_type` choices."""
        item_list = []
        content_list = ContentType.objects.all()
        for item in content_list:
            item_list.append((item.id, item.name))
        return item_list

    content_type = django_filters.ChoiceFilter(
        choices=get_content_type(), field_name='content_type__model',
        lookup_expr='iexact')
    object_id = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = models.Comment
        fields = ['content_type', 'object_id']


class CommentViewSet(viewsets.ModelViewSet):
    """Viewset for CommentSerializer."""

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = CommentFilterSet
