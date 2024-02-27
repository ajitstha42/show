from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "posts/post-list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post-detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post-form.html"
    success_url = reverse_lazy("posts:post-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        for media_file in self.request.FILES.getlist("media_files"):
            self.object.media_files.create(media=media_file)

        return response


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post-form.html"

    def get_success_url(self):
        return reverse_lazy("posts:post-detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post-delete.html"
    success_url = reverse_lazy("posts:post-list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
