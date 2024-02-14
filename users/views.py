from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("posts:post-list")
    template_name = "registration/signup.html"
