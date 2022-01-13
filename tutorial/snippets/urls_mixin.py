from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_mixin

urlpatterns = (
    path('snippets/', views_mixin.SnippetList.as_view()),
    path('snippets/<int:pk>/', views_mixin.SnippetDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)
