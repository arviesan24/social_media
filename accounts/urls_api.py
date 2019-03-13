"""Router config for Accounts APIs."""

from social_media.urls import router
from . import viewsets


router.register('profiles', viewsets.ProfileViewSet)
router.register('users', viewsets.UserViewSet)

urlpatterns = []
