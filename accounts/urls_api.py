"""Router config for Comments APIs"""

from social_media.urls import router
from .viewsets import UserViewSet


router.register('users', UserViewSet)

urlpatterns = []
