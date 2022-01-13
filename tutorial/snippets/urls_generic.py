from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_generic

urlpatterns = (
    path('snippets/', views_generic.SnippetList.as_view()),
    path('snippets/<int:pk>/', views_generic.SnippetDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)
