from django.contrib import admin
from .models import NewsPost, Comments


@admin.register(NewsPost)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    list_editable = ("user",)
    search_fields = ["title", "user__username"]
    list_filter = ("user", "created_at")

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'new', 'text', 'created_at')




