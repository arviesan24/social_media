from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import PostForm


class PostCreateView(LoginRequiredMixin, CreateView):
    """View for Creating posts."""

    form_class = PostForm
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        """Add `owner` in post."""
        post = form.save(commit=False)
        post.owner = self.request.user

        return super().form_valid(form)
