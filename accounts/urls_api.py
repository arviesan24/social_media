"""Router config for Accounts APIs."""

from social_media.urls import router
from . import viewsets


router.register('users', viewsets.UserViewSet)

urlpatterns = []
