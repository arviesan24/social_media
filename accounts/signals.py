from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from rest_framework.authtoken.models import Token

from . import models


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	"""1st way: Add @receiver decorator to trigger the signal"""
    if created:
        return Token.objects.create(user=instance)


def profile_slug(sender, instance, **kwargs):
    """Set Profile slug everytime the instance is saved."""
    if not instance.slug:
        slug_username = slugify(instance.user.username)
        str_id = str(instance.user.id)
        instance.slug = f'{slug_username}-{str_id}'


# second way: call the signal then set the function to call and the sender
pre_save.connect(profile_slug, sender=models.Profile)
