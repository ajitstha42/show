from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import CustomUser
from posts.models import Post


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("posts:post-list")
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("posts:post-list")
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


class UserProfileView(DetailView):
    model = CustomUser
    template_name = "registration/profile.html"
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = context["user_profile"]
        posts = Post.objects.filter(user=user_profile).order_by("-created_at")
        context["user_posts"] = posts
        return context
