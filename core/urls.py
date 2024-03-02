from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import send_email_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("post/", include("posts.urls", namespace="posts")),
    path("send-email/<int:post_id>/", send_email_view, name="send_email"),
    path("accounts/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
