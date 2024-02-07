from django.contrib import admin
from .models import Post, Comment, MediaFile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
