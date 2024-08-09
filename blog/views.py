from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, RegisterForm
from django.views.generic import  CreateView, UpdateView, DeleteView
from django.contrib.auth import  login 
from django.contrib.auth.decorators import login_required


# Create your views here.



def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form':form})



@login_required(login_url='/login')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})



def post_detail(request, pk):
    data = Post.objects.get(id=pk)
    post_comments = Comment.objects.filter(post=data)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = data
            myform.save()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post':data, 'form':form, 'post_comments':post_comments})


class PostCreate(CreateView):
    model = Post
    fields = ['title','content','image','tags','create_date','draft','author']
    success_url = '/blog'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content','image','tags','create_date','draft','author']
    success_url = '/blog'
    template_name = 'blog/edit_post.html'


class PostDelete(DeleteView):
    model = Post    
    success_url = '/blog'