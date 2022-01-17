from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views_viewSets import SnippetViewSet, UserViewSet, api_root

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
snippet_highight = SnippetViewSet.as_view({
    'get': 'highlight',
})
user_list = UserViewSet.as_view({
    'get': 'list',
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns((
    path('', api_root),
    path('users/', user_list, name='user-list-viewset'),
    path('users/<int:pk>/', user_detail, name='user-detail-viewset'),
    path('snippets/', snippet_list, name='snippet-list-viewset'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail-viewset'),
    path('snippets/<int:pk>/highlight/', snippet_highight,
         name='snippet-highlight-viewset'),
))
