from django.db import models
from users.models import CustomUser
from users.models import CustomUser


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Comment(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.CharField(max_length=240)
