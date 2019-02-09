"""Models for Posts app."""

from django.contrib.contenttypes.models import ContentType
from django.db import models

from comments.models import Comment


class Post(models.Model):
    """Model for Posts."""

    CHOICE_PRIVATE = 'private'
    CHOICE_FRIENDS = 'only friends'
    CHOICE_PUBLIC = 'public'

    PRIVACY_CHOICES = (
        (CHOICE_PRIVATE, 'Private'),
        (CHOICE_FRIENDS, 'Only friends'),
        (CHOICE_PUBLIC, 'Public'),
    )

    owner = models.ForeignKey(
        'accounts.User', related_name='posts',
        related_query_name='post', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    @property
    def comments(self):
        """Return all comments associated to the post."""
        qs = Comment.objects.filter_by_instance(self)
        return qs
