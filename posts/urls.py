from django.urls import path
from .views import PostListView, get_additional_media


app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path(
        "get_additional_media/<int:post_id>/",
        get_additional_media,
        name="get_additional_media",
    ),
]
