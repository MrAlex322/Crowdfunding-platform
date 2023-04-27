from django.contrib.auth import authenticate, login
from users.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import NewsPost
from .forms import NewsPostForm


# Create your views here.


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def news_list(request):
    posts = NewsPost.objects.all()
    return render(request, 'news/news_list.html', {
        "posts": posts,
    })


def create_news_post(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsPostForm()
        news_form = {
            'form': form,
        }
    return render(request, 'news/create_news_post.html', news_form)



