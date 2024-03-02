from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .mixins import RecruiterAccessMixin
from .models import Post
from .forms import PostForm, EmailForm


class PostListView(ListView):
    model = Post
    template_name = "posts/post-list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post-detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, RecruiterAccessMixin, CreateView):
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


@login_required
def send_email_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user.role != "recruiter":
        messages.error(request, "Only Recruiters can send emails.")
        return redirect(reverse("posts:post-list"))

    recruiter_email = request.user.email
    recruit_email = post.user.email

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            send_mail(subject, message, recruiter_email, [recruit_email])

            messages.success(request, "Email sent successfully!")
            return redirect("posts:post-list")
    else:
        default_subject = f"Regarding your job application for '{post.title}'"
        default_message = f"Dear {post.user.username},\n\n"
        form = EmailForm(
            initial={"subject": default_subject, "message": default_message}
        )

    return render(
        request, "send_email.html", {"form": form, "recruit_email": recruit_email}
    )
