"""Forms for `comments` app."""

from django import forms

from django.models import Comment


class CommentForm(forms.ModelForm):
    """Form for Comment."""

    class Meta:
        model = Comment
        fields = (
            'content_type', 'object_id', 'content_object',
            'parent', 'content')
