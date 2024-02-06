from django.contrib import admin
from .models import Post, Comment, MediaFile

# Register your models here.


@admin.register(Post)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(MediaFile)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CustomUserAdmin(admin.ModelAdmin):
    pass
