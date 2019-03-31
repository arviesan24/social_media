"""Models for Images app."""

from django.contrib.contenttypes.models import ContentType
from django.db import models

from comments.models import Comment


class Image(models.Model):
    """Model for user uploaded images."""

    CHOICE_PRIVATE = 'private'
    CHOICE_FRIENDS = 'only friends'
    CHOICE_PUBLIC = 'public'

    PRIVACY_CHOICES = (
        (CHOICE_PRIVATE, 'Private'),
        (CHOICE_FRIENDS, 'Only friends'),
        (CHOICE_PUBLIC, 'Public'),
    )

    location = models.ImageField()
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey(
        'Album', on_delete=models.PROTECT, related_name='images',
        related_query_name='image')
    privacy = models.CharField(max_length=7,choices=PRIVACY_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    @property
    def comments(self):
        """Return all comments associated to the image."""
        qs = Comment.objects.filter_by_instance(self)
        return qs

    @property
    def get_content_type(self):
        """Return model class."""
        content_type = ContentType.objects.get_for_model(self.__class__)
        return content_type


class Album(models.Model):
    """Model for image albums."""

    CHOICE_FRIEND = 'friend'
    CHOICE_PRIVATE = 'private'
    CHOICE_PUBLIC = 'public'

    PRIVACY_CHOICES = (
        (CHOICE_FRIEND, 'Friends'),
        (CHOICE_PRIVATE, 'Only Me'),
        (CHOICE_PUBLIC, 'Public'),
    )

    owner = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='folders',
        related_query_name='folder')
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    privacy = models.CharField(max_length=7,choices=PRIVACY_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
