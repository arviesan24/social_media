"""Forms for `comments` app."""

from django import forms
from django.contrib.contenttypes.models import ContentType

from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for Comment."""

    content_type = forms.CharField(required=False)

    class Meta:
        model = Comment
        fields = ('content_type', 'object_id', 'parent', 'content')
