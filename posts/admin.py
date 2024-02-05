from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CustomUserAdmin(admin.ModelAdmin):
    pass
