from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls import reverse_lazy


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',
        LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]
