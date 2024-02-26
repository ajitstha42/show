from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

from .forms import CustomUserCreationForm, CustomUserChangeForm
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


class UserProfileView(UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = "registration/profile.html"
    context_object_name = "user_profile"

    def test_func(self):

        user_profile = self.get_object()
        return (
            self.request.user == user_profile
            or self.request.user.role == CustomUser.RECRUITER
        )

    def handle_no_permission(self):
        return render(self.request, "403.html", status=403)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = context["user_profile"]

        can_view_cv_and_resume = self.test_func()

        if can_view_cv_and_resume:
            context["user_posts"] = Post.objects.filter(user=user_profile).order_by(
                "-created_at"
            )
            context["can_view_cv_and_resume"] = True
        else:
            context["can_view_cv_and_resume"] = False

        return context


class UpdateProfileView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "registration/update_profile.html"

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.kwargs["pk"])

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.object.pk})
