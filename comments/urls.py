from django.urls import path

from . import views


urlpatterns = [
    path(
        'create/', views.PostCommentCreateView.as_view(),
        name='create-comment'),
]
