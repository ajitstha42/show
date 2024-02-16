from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from .models import CustomUser
from posts.models import Post


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("posts:post-list")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "registration/profile.html"
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = context["user_profile"]
        posts = Post.objects.filter(user=user_profile).order_by("-created_at")
        context["user_posts"] = posts
        return context
