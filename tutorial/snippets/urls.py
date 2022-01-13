from django.urls import path
from snippets.views import UserList, UserDetail, SnippetList, SnippetDetail

urlpatterns = (
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
)
