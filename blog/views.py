from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.



class PostList(ListView):    # template : post_list
    model = Post             # contexe  : post_list , object_list



def post_detail(request, pk):
    data = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post':data})


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