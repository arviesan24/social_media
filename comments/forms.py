"""Forms for `comments` app."""

from django import forms
from django.contrib.contenttypes.models import ContentType

from django.models import Comment


class CommentForm(forms.ModelForm):
    """Form for Comment."""

    def __init__(self, *args, **kwargs):
        """Initialize `content_type_value` from views."""
        self.content_type_value = kwargs.pop('content_type_value', None)
        super().__init__(*args, **kwargs)

    content_type = forms.CharField(required=False)

    class Meta:
        model = Comment
        fields = (
            'content_type', 'object_id', 'content_object',
            'parent', 'content')
