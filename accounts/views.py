from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import User


class ProfileView(DetailView):
    """View for User Profile"""

    template_name='accounts/profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
