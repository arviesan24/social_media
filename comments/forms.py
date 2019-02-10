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
        fields = ('content_type', 'object_id', 'parent', 'content')

    def clean_content_type(self):
        """Get `content_type` from `__init__` instead from templates form."""
        content_type = ContentType.objects.get(model=self.content_type_value)
        if not content_type:
            raise forms.ValidationError('Invalid content type.')

        return content_type
