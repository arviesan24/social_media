"""Router config for Accounts APIs."""

from social_media.urls import router
from . import viewsets


router.register('profiles', viewsets.ProfileViewSet)
router.register('relationships', viewsets.RelationshipViewSet)
router.register('relationship-types', viewsets.RelationshipTypeViewSet)
router.register('requests', viewsets.RequestViewSet)
router.register('users', viewsets.UserViewSet)

urlpatterns = []
