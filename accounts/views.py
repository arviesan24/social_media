from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from .forms import RegisterForm
from .forms import ProfileForm

from .models import Profile
from .models import User

from comments import forms as comment_form

from posts import forms as post_form
from posts import models as post_model


class MyProfileView(LoginRequiredMixin, DetailView):
    """View for User Profile."""

    template_name='accounts/my_profile.html'

    def get_object(self):
        """Get user object without using URL kwargs."""
        return get_object_or_404(Profile, user__id=self.request.user.id)
    
    def get_context_data(self, **kwargs):
        """Retuns context data needed in `Profile`"""
        kwargs = super().get_context_data()
        # add `post form` in context data
        kwargs['post_form'] = post_form.PostForm
        # add `post list` in context data
        kwargs['post_list'] = (
            post_model.Post.objects.filter(
                owner=self.request.user).order_by('-id'))
        # add `comment form` in context data
        kwargs['comment_form'] = comment_form.CommentForm
        return kwargs


class ProfileView(LoginRequiredMixin, DetailView):
    """View for other User's Profile."""

    template_name = 'accounts/profile.html'
    model = Profile


class RegisterView(CreateView):
    """View for User Registration"""

    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')


class CreateProfileView(LoginRequiredMixin, CreateView):
    """View for Create Profile"""

    template_name = 'accounts/create_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('accounts:my-profile')

    def dispatch(self, request, *args, **kwargs):
        """Redirect to create profile form if user has no profile set."""
        if Profile.objects.filter(user__id=request.user.id):
            return HttpResponseRedirect(
                reverse_lazy('accounts:my-profile'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Save profile for current user."""
        response = form.save(commit=False)
        response.user = self.request.user
        
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Insert the dropdown options into the context dict."""
        context = {}
        context['preferences'] = Profile.PREFERENCE_CHOICES
        context['genders'] = Profile.GENDER_CHOICES
        context.update(kwargs)
        return super().get_context_data(**context)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """View for Update Profile"""

    template_name = 'accounts/edit_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('accounts:my-profile')

    def get_object(self, queryset=None):
        """
        Get current user object.
        """
        return get_object_or_404(Profile, user__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        """Insert the dropdown options into the context dict."""
        context = {}
        context['preferences'] = Profile.PREFERENCE_CHOICES
        context['genders'] = Profile.GENDER_CHOICES
        context.update(kwargs)
        return super().get_context_data(**context)
