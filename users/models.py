from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class NewsPost(models.Model):
    header = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    number_of_views = models.IntegerField()
    body = models.TextField()
    slug = models.SlugField(default='', null=False, db_index=True)


    def __str__(self):
        return f'{self.header} - {self.author} - {self.body}%'
