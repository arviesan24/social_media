from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class CommentManager(models.Manager):
    """Model manager for `Comment` model."""

    def all(self):
        """Return results of instance with no parent (not a reply)."""
        qs = super().filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        """Return result base on model class passed (not a reply)."""
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super().filter(
            content_type=content_type, object_id=obj_id, parent=None)
        return qs


class Comment(models.Model):
    """Model for comments."""

    owner = models.ForeignKey(
        'accounts.User', related_name='comments',
        related_query_name='comment', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # If not null, instance is a reply.
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    objects = CommentManager()

    def children(self):
        """Return replies of a comment."""
        return Comment.objects.filter(parent=self)
