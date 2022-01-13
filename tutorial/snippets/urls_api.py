from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_api

urlpatterns = (
    path('snippets/', views_api.SnippetList.as_view()),
    path('snippets/<int:pk>/', views_api.SnippetDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)
