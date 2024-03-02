from django import forms
from multiupload.fields import MultiFileField
from .models import Post


class PostForm(forms.ModelForm):
    media_files = MultiFileField(max_num=10, max_file_size=1024 * 1024 * 5)

    class Meta:
        model = Post
        fields = ["title", "description", "media_files"]


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
