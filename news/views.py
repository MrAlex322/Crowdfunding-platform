from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from .models import NewsPost
from .forms import NewsPostForm
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


def create_news_post(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
        news_form = {
            'form': form,
        }
    return render(request, 'news/create_news_post.html', news_form)


def view_news_post(request, slug):
    post = get_object_or_404(NewsPost, slug=slug)

    return render(request, 'news/view_news_post.html', {'post': post})


def edit_news_post(request, slug):
    # Получаем новостной пост по заголовку
    post = get_object_or_404(NewsPost, slug=slug)

    if request.method == 'POST':
        form = NewsPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsPostForm(instance=post)

    return render(request, 'news/edit_news_post.html', {'form': form})

