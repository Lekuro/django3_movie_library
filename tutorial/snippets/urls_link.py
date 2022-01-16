from django.urls import path
from snippets import views_link
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns((
    path('', views_link.api_root),
    path('snippets/<int:pk>/highlight/',
         views_link.SnippetHighlight.as_view(),
         name='snippet-highlight'),
))
