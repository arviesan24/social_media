from django.urls import path

from . import views


urlpatterns = [
    path('',
        views.NewsFeedTemplateView.as_view(),name='list'),
]
