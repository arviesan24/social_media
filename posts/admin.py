from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    """Post model admin."""
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
