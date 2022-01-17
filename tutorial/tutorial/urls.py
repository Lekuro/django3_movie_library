"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from snippets.views_viewSets import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('quick/', include('quickstart.urls')),
    path('', include('snippets.urls')),
    path('def/', include('snippets.urls_def')),
    path('def-api/', include('snippets.urls_def_api')),
    path('api/', include('snippets.urls_api')),
    path('mixin/', include('snippets.urls_mixin')),
    path('generic/', include('snippets.urls_generic')),
    path('link/', include('snippets.urls_link')),
    # path('viewset/', include('snippets.urls_viewSets')),
    path('viewset/', include(router.urls)),
)
