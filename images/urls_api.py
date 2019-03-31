"""Router config for Images APIs"""

from social_media.urls import router

from . import viewsets


router.register('albums', viewsets.AlbumViewSet)
router.register('images', viewsets.ImageViewSet)

urlpatterns = []
