from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import reverse_lazy

from . import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/',
        LogoutView.as_view(next_page=reverse_lazy('accounts:login')),
        name='logout'),
    path(
        'create-profile/',
        views.CreateProfileView.as_view(), name='create-profile'),
    path(
        'edit-profile/',
        views.UpdateProfileView.as_view(), name='edit-profile'),
    path('my-profile/', views.MyProfileView.as_view(), name='my-profile'),
    path('profile/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
