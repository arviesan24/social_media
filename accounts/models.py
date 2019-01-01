from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractUser):
    """Model Extending AbstractUser."""

    CHOICE_MALE = 'm'
    CHOICE_FEMALE = 'f'

    CHOICE_MEN = 'men'
    CHOICE_WOMEN = 'women'
    CHOICE_BOTH = 'both'

    GENDER_CHOICES = (
        (CHOICE_MALE, 'Male'),
        (CHOICE_FEMALE, 'Female'),
    )

    PREFERENCE_CHOICES = (
        (CHOICE_MEN, 'Men'),
        (CHOICE_WOMEN, 'Women'),
        (CHOICE_BOTH, 'Both'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    preference = models.CharField(max_length=5, choices=PREFERENCE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


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
