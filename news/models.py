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
    slug = AutoSlugField(default='', unique=False, populate_from='title')
    user = models.ForeignKey(CustomUser, to_field='username', verbose_name='Пользователь', on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(CustomUser, related_name='disliked_posts', blank=True)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)

    def increase_likes(self):
        self.likes_count += 1
        self.save()

    def decrease_likes(self):
        if self.likes_count > 0:
            self.likes_count -= 1
            self.save()

    def increase_dislikes(self):
        self.dislikes_count += 1
        self.save()

    def decrease_dislikes(self):
        if self.dislikes_count > 0:
            self.dislikes_count -= 1
            self.save()

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


