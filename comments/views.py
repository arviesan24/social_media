"""Views for `comments` app."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CommentForm


class PostCommentCreateView(LoginRequiredMixin, CreateView):
    """View for Comment creation."""

    form_class = CommentForm
    success_url = reverse_lazy('accounts:profile')

    def get_form_kwargs(self):
        """Pass `content_type_value` value to `CommentForm`."""
        kwargs = super().get_form_kwargs()
        kwargs['content_type_value'] = 'post'
        return kwargs 

    def form_valid(self, form):
        """Save comment."""
        comment = form.save(commit=False)
        comment.object_id = form.cleaned_data.get('object_id')
        comment.parent = None
        comment.owner = self.request.user
        return super().form_valid(form)
