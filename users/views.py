from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from news.models import NewsPost
from users.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View



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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)



@login_required
def profile(request):
    user = request.user
    posts = NewsPost.objects.filter(user=user)

    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserCreationForm(instance=user)

    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'profile.html', context)



