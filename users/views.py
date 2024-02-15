from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("posts:post-list")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
