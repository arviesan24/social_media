"""Views for `newsfeeds` app."""

from actstream.models import user_stream
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView

from accounts.models import Profile


class NewsFeedListView(LoginRequiredMixin, ListView):
    """ListView containing `user_stream` instances."""

    template_name = 'newsfeeds/list.html'
    context_object_name = 'feeds'

    def get_context_data(self, **kwargs):
        """Return context data to the template."""
        context = super().get_context_data(**kwargs)
        usr_stream = user_stream(
            self.request.user).prefetch_related('actor', 'action_object')
        # add `user_stream` to context variable.
        context['feeds'] = usr_stream

        return context
