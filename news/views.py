from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import NewsPost, Comments
from .forms import NewsPostForm, CommentForm
from django.utils.text import slugify


def news_list(request):
    posts = NewsPost.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'news/news_list.html', context)


@login_required
def create_news_post(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            newspost = form.save(commit=False)
            newspost.user = request.user
            newspost.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
        context = {
            'form': form,
        }

    return render(request, 'news/create_news_post.html', context)


def view_news_post(request, slug):
    new = get_object_or_404(NewsPost, slug=slug)
    comments = Comments.objects.filter(new=new)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect('view_news_post', slug)
    else:
        form = CommentForm()

    likes_count = new.likes.count()
    dislikes_count = new.dislikes.count()

    context = {
        "new": new,
        "comments": comments,
        "form": form,
        "likes_count": likes_count,
        "dislikes_count": dislikes_count,
    }
    return render(request, 'news/view_news_post.html', context)


def edit_news_post(request, slug):
    post = get_object_or_404(NewsPost, slug=slug)

    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsPostForm(instance=post)

    return render(request, 'news/edit_news_post.html', {'form': form})


def like_post(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('news_list')


def dislike_post(request, post_id):
    post = get_object_or_404(NewsPost, id=post_id)
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return redirect('news_list')
