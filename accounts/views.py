from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import RegisterForm

from .models import User


class ProfileView(LoginRequiredMixin, DetailView):
    """View for User Profile"""

    template_name='accounts/profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)


class RegisterView(CreateView):
    """View for User Registration"""

    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
