from django.urls import path
from snippets import views_def

urlpatterns = (
    path('snippets/', views_def.snippet_list),
    path('snippets/<int:pk>/', views_def.snippet_detail),
)
