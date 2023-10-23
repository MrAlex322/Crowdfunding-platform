from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from news.models import CustomUser

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")
