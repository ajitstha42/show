from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.forms.widgets import DateInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
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

    dob = forms.DateField(
        widget=forms.TextInput(attrs={"class": "form-control", "type": "date"}),
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "avatar",
            "email",
            "cv",
            "resume",
            "bio",
            "dob",
        ]

    def clean_cv(self):
        cv = self.cleaned_data["cv"]
        if cv:
            if not cv.name.lower().endswith(".pdf"):
                raise forms.ValidationError("Please upload a PDF file for CV.")
        return cv

    def clean_resume(self):
        resume = self.cleaned_data["resume"]
        if resume:
            if not resume.name.lower().endswith(".pdf"):
                raise forms.ValidationError("Please upload a PDF file for Resume.")
        return resume
