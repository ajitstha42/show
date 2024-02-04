from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    cv = models.FileField(upload_to="cv/")
    resume = models.FileField(upload_to="cv/")
    avatar = models.ImageField(upload_to="images/", default="image/default.png")
    email = models.EmailField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
