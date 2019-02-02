"""Router config for Comments APIs"""

from social_media.urls import router
from .viewsets import CommentViewSet


router.register('comments', CommentViewSet)

urlpatterns = []
