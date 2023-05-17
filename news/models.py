from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.urls import reverse


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='my_model_photos/', blank=True, null=True)
    slug = AutoSlugField(default='', unique=False, populate_from='title')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('view_news_post', args=[self.slug])

    def __str__(self):
        return self.title
