from django import forms
from .models import Post
from martor.widgets import MartorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': MartorWidget,
        }