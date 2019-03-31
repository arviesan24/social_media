"""Admin for Images app."""

from django.contrib import admin

from . import models


admin.site.register(models.Album)
admin.site.register(models.Image)
