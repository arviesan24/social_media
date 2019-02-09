"""Router config for Posts APIs."""

from social_media.urls import router
from .viewsets import PostViewSet


router.register('posts', PostViewSet)

urlpatterns = []
