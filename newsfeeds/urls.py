from django.urls import path

from . import views


urlpatterns = [
    path('',
        views.NewsFeedListView.as_view(),name='list'),
]
