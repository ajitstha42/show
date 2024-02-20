from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from users.models import CustomUser


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse("posts:post-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class MediaFile(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="media_files")
    media = models.FileField(
        upload_to="media/",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "mp4", "mkv"])
        ],
    )


class Comment(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.CharField(max_length=240)
