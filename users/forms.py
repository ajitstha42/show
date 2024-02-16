from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "password1",
            "password2",
            "username",
            "avatar",
            "email",
            "role",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "avatar",
            "email",
            "role",
            "cv",
            "resume",
            "bio",
            "dob",
        ]
