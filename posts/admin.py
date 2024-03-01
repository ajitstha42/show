from django.contrib import admin
from .models import Post, Comment, MediaFile


class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 2


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        MediaFileInline,
    ]


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
