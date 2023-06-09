from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.urls import reverse

from users.models import CustomUser


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='my_model_photos/', blank=True, null=True)
    slug = AutoSlugField(default='', unique=False, populate_from='title') # проверить если тайтл = цифры
    user = models.ForeignKey(CustomUser, to_field='username', verbose_name='Пользователь', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsPost, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('view_news_post', args=[self.slug])

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, to_field='username', verbose_name='Пользователь', on_delete=models.CASCADE)
    new = models.ForeignKey(NewsPost, verbose_name="Новость", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.user)
