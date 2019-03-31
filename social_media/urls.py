"""social_media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView

from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/',
        include(('accounts.urls', 'accounts'), namespace="accounts")),
    path('comments/',
        include(('comments.urls', 'comments'), namespace="comments")),
    path('posts/',
        include(('posts.urls', 'posts'), namespace="posts")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),

    # DRF URLs
    path('', include('comments.urls_api')),
    path('', include('accounts.urls_api')),
    path('', include('images.urls_api')),
    path('', include('posts.urls_api')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    urlpatterns = (
        urlpatterns + static(
            settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
