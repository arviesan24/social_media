"""Views for `comments` app."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CommentForm


class BasePostCommentCreateView(LoginRequiredMixin, CreateView):
    """Base view for comment CreateView"""

    form_class = CommentForm
    success_url = reverse_lazy('accounts:my-profile')

    def get_form_kwargs(self):
        """Pass `content_type_value` value to `CommentForm`."""
        kwargs = super().get_form_kwargs()
        kwargs['content_type_value'] = 'post'
        return kwargs 


class PostCommentCreateView(BasePostCommentCreateView):
    """View for Post Comment creation."""

    def form_valid(self, form):
        """Save comment."""
        comment = form.save(commit=False)
        comment.object_id = form.cleaned_data.get('object_id')
        comment.parent = None
        comment.owner = self.request.user
        return super().form_valid(form)


class PostReplyCreateView(BasePostCommentCreateView):
    """View for Post Reply creation."""

    def form_valid(self, form):
        """Save comment."""
        comment = form.save(commit=False)
        comment.object_id = form.cleaned_data.get('object_id')
        comment.parent.id = form.cleaned_data.get('parent')
        comment.owner = self.request.user
        return super().form_valid(form)
