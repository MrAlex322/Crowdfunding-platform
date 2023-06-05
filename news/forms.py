from django import forms
from .models import NewsPost
from django.forms import ModelForm
from .models import Comments


class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'content', 'photo']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text', )