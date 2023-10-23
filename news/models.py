from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.urls import reverse

CustomUser = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey('NewsPost', on_delete=models.CASCADE)


class Dislike(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey('NewsPost', on_delete=models.CASCADE)


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='my_model_photos/', blank=True, null=True)
    slug = AutoSlugField(default='', unique=False, populate_from='title')
    user = models.ForeignKey(CustomUser, to_field='username', verbose_name='Пользователь', on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', through=Like)
    dislikes = models.ManyToManyField(CustomUser, related_name='disliked_posts', through=Dislike)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsPost, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('view_news_post', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


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
