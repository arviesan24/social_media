"""Router config for Comments APIs"""

from social_media.urls import router

from .viewsets import CommentViewSet
from .viewsets import ReplyViewSet


router.register('comments', CommentViewSet)
router.register('replies', ReplyViewSet)

urlpatterns = []
