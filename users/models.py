from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    cv = models.FileField(upload_to="cv/")
    bio = models.TextField(default="")
    resume = models.FileField(upload_to="cv/")
    avatar = models.ImageField(upload_to="images/", default="image/default.png")
    dob = models.DateField(null=True)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
