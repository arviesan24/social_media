from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """Model Extending AbstractBaseUser."""

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username' # used for login field
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    is_active(self):
        return self.active


class Relationship(models.Model):
    """Model for Relationship."""

    CHOICE_BLOCKED = 'blocked'
    CHOICE_FRIEND = 'friend'
    CHOICE_PARTNER = 'partner'

    TYPE_CHOICES = (
        (CHOICE_BLOCKED, 'Blocked'),
        (CHOICE_FRIEND, 'Friend'),
        (CHOICE_PARTNER, 'Partner'),
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='sent_relationships',
        related_query_name='sent_relationship')
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='receive_relationships',
        related_query_name='receive_relationship')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Request(models.Model):
    """Model for Request."""

    CHOICE_PENDING = 'pending'
    CHOICE_CONFIRMED = 'confirmed'

    STATUS_CHOICES = (
        (CHOICE_PENDING, 'Pending'),
        (CHOICE_CONFIRMED, 'Confirmed'),
    )

    relationship = models.ForeignKey('Relationship', on_delete=models.CASCADE,
        related_name='requests',
        related_query_name='request')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
