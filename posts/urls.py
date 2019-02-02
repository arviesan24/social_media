from django.urls import path
from django.urls import reverse_lazy

from . import views


urlpatterns = [
    path('create/',
        views.PostCreateView.as_view(),name='create-post'),
]
