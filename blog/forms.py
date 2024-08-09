from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200 , required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author",)

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

