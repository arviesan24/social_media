"""Router config for Comments APIs"""

from social_media.urls import router

from . import viewsets


router.register('comments', viewsets.CommentViewSet)

urlpatterns = []
