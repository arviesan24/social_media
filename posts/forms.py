from django import forms

from django_summernote.widgets import SummernoteInplaceWidget
from django_summernote.widgets import SummernoteWidget

from .models import Post


class PostForm(forms.ModelForm):
    """Form for Post model."""

    class Meta:
        model = Post
        fields = ['content', 'privacy']
        widgets = {
            'content': SummernoteWidget(),
        }
