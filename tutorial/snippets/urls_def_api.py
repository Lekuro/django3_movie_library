from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_def_api

urlpatterns = (
    path('snippets/', views_def_api.snippet_list),
    path('snippets/<int:pk>/', views_def_api.snippet_detail),
)
urlpatterns = format_suffix_patterns(urlpatterns)
