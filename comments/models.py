from django.db import models


class Comment(models.Model):
    """Model for comments."""

    owner = models.ForeignKey(
        'accounts.User', related_name='posts',
        related_query_name='post', on_delete=models.CASCADE)
    post = models.ForeignKey(
        'posts.Post', related_name='comments',
        related_query_name='comment', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Reply(models.Model):
    """Model for replies."""

    owner = models.ForeignKey(
        'accounts.User', related_name='replies',
        related_query_name='reply', on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'Comment', related_name='replies',
        related_query_name='reply', on_delete=models.CASCADE)
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
