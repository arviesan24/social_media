from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls import reverse_lazy

from . import views


urlpatterns = [
    path('login/',
        LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',
        LogoutView.as_view(next_page=reverse_lazy('accounts:login')),
        name='logout'),
    path(
        'create-profile/',
        views.CreateProfileView.as_view(), name='create-profile'),
    path(
        'edit-profile/',
        views.UpdateProfileView.as_view(), name='edit-profile'),
    path('profile/', views.MyProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
