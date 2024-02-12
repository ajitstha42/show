from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.http import JsonResponse


def get_additional_media(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        additional_media_files = [media.media.url for media in post.media_files.all()]
    except Post.DoesNotExist:
        additional_media_files = []

    data = {
        "additionalMediaFiles": additional_media_files,
    }

    return JsonResponse(data)


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post-list.html"
    context_object_name = "posts"
