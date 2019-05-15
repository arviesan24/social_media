"""Posts app's views."""

import json

from actstream import action
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import PostForm


class PostCreateView(LoginRequiredMixin, CreateView):
    """View for Creating posts."""

    form_class = PostForm
    success_url = reverse_lazy('accounts:my-profile')

    def form_valid(self, form):
        """Add `owner` in post."""
        post = form.save(commit=False)
        post.owner = self.request.user
        response = super().form_valid(form)
        # send actstream signal
        action.send(
            self.request.user, verb='created a new post',
            action_object=self.object)

        return response
