from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import RegisterForm

from .models import Profile
from .models import User


class ProfileView(LoginRequiredMixin, DetailView):
    """View for User Profile"""

    template_name='accounts/profile.html'
    login_url = reverse_lazy('accounts:login')

    def get_object(self):
        """Get user object without using URL kwargs."""
        return get_object_or_404(User, pk=self.request.user.id)

    def dispatch(self, request, *args, **kwargs):
        """Redirect to create profile form if user has no profile set."""
        if Profile.objects.filter(id=request.user.id):
            return HttpResponseRedirect(
                reverse_lazy('accounts:create_profile'))
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    """View for User Registration"""

    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
