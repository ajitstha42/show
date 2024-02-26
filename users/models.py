from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    RECRUIT = "recruit"
    RECRUITER = "recruiter"

    ROLE_CHOICES = [
        (RECRUIT, "Recruit"),
        (RECRUITER, "Recruiter"),
    ]

    username = models.CharField(unique=True, max_length=50)
    cv = models.FileField(upload_to="cv/", null=True, blank=True)
    bio = models.TextField(default="", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", null=True, blank=True)
    avatar = models.ImageField(upload_to="images/", default="default.jpg")
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    def has_cv(self):
        return bool(self.cv)

    def has_resume(self):
        return bool(self.resume)
