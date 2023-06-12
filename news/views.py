from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from users.models import CustomUser
from .models import NewsPost, Comments
from .forms import NewsPostForm, CommentForm
from django.utils.text import slugify

def news_list(request):
    posts = NewsPost.objects.all()
    for post in posts:
        if not post.slug:
            post.slug = slugify(post.title)
            post.save()
    slugs = [post.slug for post in posts]
    return render(request, 'news/news_list.html', {
        "posts": posts,
    })

@login_required
def create_news_post(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            newspost = form.save(commit=False)
            newspost.user = request.user  # Используйте текущего аутентифицированного пользователя
            newspost.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
        news_form = {
            'form': form,
        }

    return render(request, 'news/create_news_post.html', news_form)


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
    context = {
        "new": new,
        "comments": comments,
        "form": form,
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

