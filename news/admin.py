from django.contrib import admin
from .models import NewsPost


@admin.register(NewsPost)
class NewsAdmin(admin.ModelAdmin):
    pass
