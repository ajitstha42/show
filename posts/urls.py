from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
)

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # Detail view
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    # path("<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
