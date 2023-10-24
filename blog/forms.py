from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)
        widgets = {
            'content': SummernoteWidget(),
        }

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

