from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
"""
https://docs.djangoproject.com/en/2.1/topics/http/decorators/

require_POST : POST메소드만 허용하도록 하는 데코레이터
require_safe : GET & HEAD method만 허용하는 데코레이터

"""

# Create your views here.
def create(request):
    if request.method == "POST":
        # modelform을 통해서 Post를 만들어줌.
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully uploaded!")
            return redirect("posts:list")
        else:
            messages.error(request, "request denied!")
            return redirect("posts:create")
    else:
        # modelform을 전달해서 form을 보여줌.
        form = PostModelForm()
        return render(request, 'posts/create.html', {
            'form' : form
        })

def list(request):
    posts = Post.objects.all()
    form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts' : posts,
        'form' : form
    })

def delete(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    if request.user != p.user:
        return redirect('posts:list')
    p.delete()
    return redirect('posts:list')
    
def update(request, post_id):
    p = get_object_or_404(Post, id=post_id)
    if request.user != p.user:
        return redirect('posts:list')
    
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully modified!")
            return redirect('posts:list')
        else:
            messages.error(request, "request denied!")
            return redirect('posts:create')
    else:
        form = PostModelForm(instance=p)
        return render(request, 'posts/create.html', {
            'form' : form
        })

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    u = request.user
    if post in u.like_posts.all():
        u.like_posts.remove(post)
    else:
        u.like_posts.add(post)

    return redirect('posts:list')
    
@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = post.id
        comment.user_id = request.user.id
        comment.save()
    return redirect('posts:list')
    

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('posts:list')
    