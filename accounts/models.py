from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

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
    slug = models.SlugField(null=True)
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

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='sent_relationships',
        related_query_name='sent_relationship')
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='receive_relationships',
        related_query_name='receive_relationship')
    request = models.ForeignKey('Request', on_delete=models.PROTECT,
        related_name='relationships',
        related_query_name='relationship', null=True)
    type = models.ForeignKey('RelationshipType', on_delete=models.PROTECT,
        related_name='relationships',
        related_query_name='relationship')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class RelationshipType(models.Model):
    """Model for Relationship types."""

    name = models.CharField(max_length=50, unique=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Request(models.Model):
    """Model for Relationship requests."""

    status = models.CharField(max_length=50, unique=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        return Token.objects.create(user=instance)


def profile_slug(sender, instance, **kwargs):
    """Set Profile slug everytime the instance is saved."""
    if not instance.slug:
        slug_username = slugify(instance.user.username)
        str_id = str(instance.user.id)
        instance.slug = f'{slug_username}-{str_id}'

pre_save.connect(profile_slug, sender=Profile)
