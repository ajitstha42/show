from django.views.generic import ListView, DetailView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post-detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("posts:post-detail")


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("posts:post-detail")
