from django import forms
from multiupload.fields import MultiFileField
from .models import Post


class PostForm(forms.ModelForm):
    media_files = MultiFileField(max_num=10, max_file_size=1024 * 1024 * 5)

    class Meta:
        model = Post
        fields = ["title", "description", "media_files"]
