"""DRF URLS"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from rest_framework import routers


router = routers.SimpleRouter()

urlpatterns = [
    path('', include('comments.urls_api')),

    path('api/', include('rest_framework.urls')),
]


if settings.DEBUG:
    urlpatterns = (
        urlpatterns + static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
