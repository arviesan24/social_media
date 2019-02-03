from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    """Model Extending AbstractBaseUser."""

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username' # used for login field
    REQUIRED_FIELDS = ['email']


class Profile(models.Model):
    """Model for Profile."""

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
    
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    gender = models.CharField(
        max_length=1, blank=False, null=False, choices=GENDER_CHOICES)
    preference = models.CharField(max_length=5, choices=PREFERENCE_CHOICES)
    birth_date = models.DateField(blank=False, null=False)
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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
