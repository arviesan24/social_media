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
    paginate_by = 50

    def get_queryset(self):
        """Returns listview's queryset."""
        # use `actstream.user_stream` as the listview queryset
        usr_stream = user_stream(
            self.request.user).prefetch_related('actor', 'action_object')

        return usr_stream
