"""Router config for Accounts APIs."""

from social_media.urls import router
from .viewsets import UserViewSet


router.register('users', UserViewSet)

urlpatterns = []
