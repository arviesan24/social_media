"""Viewsets for Comments app."""
from django.contrib.contenttypes.models import ContentType
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow object owner to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the owner of the snippet.
#         return obj.owner == request.user


# class ImageFilterSet(django_filters.FilterSet):
#     """FilterSet for CommentViewSet."""

#     def get_content_type():
#         """Return list for `content_type` choices."""
#         item_list = []
#         content_list = ContentType.objects.all()
#         for item in content_list:
#             item_list.append((item.name, item.name))
#         return item_list

#     def get_is_parent(self, queryset, name, value):
#         """Filters queryset based on `is_parent` field."""
#         if value == True:
#             queryset = queryset.filter(parent__isnull=True)
#         else:
#             queryset = queryset.filter(parent__isnull=False)

#         return queryset

#     is_parent = django_filters.BooleanFilter(method='get_is_parent')
#     content_type = django_filters.ChoiceFilter(
#         choices=get_content_type(), field_name='content_type__model',
#         lookup_expr='iexact')
#     object_id = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = models.Comment
#         fields = ['content_type', 'object_id', 'parent__id', 'is_parent']


class ImageViewSet(viewsets.ModelViewSet):
    """Viewset for CommentSerializer."""

    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    # filterset_class = CommentFilterSet


class AlbumViewSet(viewsets.ModelViewSet):
    """Viewset for CommentSerializer."""

    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    # filterset_class = CommentFilterSet
