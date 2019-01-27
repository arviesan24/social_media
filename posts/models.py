from django.db import models


class Post(models.Model):
    """Model for Posts."""

    CHOICE_PRIVATE = 'private'
    CHOICE_FRIENDS = 'only friends'
    CHOICE_PUBLIC = 'public'

    PRIVACY_CHOICES = (
        (CHOICE_PRIVATE, 'Private'),
        (CHOICE_FRIENDS, 'Only friends'),
        (CHOICE_PUBLIC, 'public'),
    )

    owner = models.ForeignKey(
        'accounts.User', related_name='posts',
        related_query_name='post', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
