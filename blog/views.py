from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    data = Post.objects.all()
    return render(request, 'post_list.html', {'posts':data})


def post_details(request, post_id):
    data = Post.objects.get(id=post_id)
    return render(request, 'post_details.html', {'post':data})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form':form})


def edit_post(request, post_id):
    pass


def delete_post(request, post_id):
    pass
