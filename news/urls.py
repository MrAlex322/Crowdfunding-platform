from django.urls import path
from . import views
from .views import view_news_post, edit_news_post


urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('create_news_post/', views.create_news_post, name='create_news_post'),
    path('edit_news_post/<slug:slug>/', views.edit_news_post, name='edit_news_post'),
    path('<slug:slug>/', view_news_post, name='view_news_post'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike-post/<int:post_id>/', views.dislike_post, name='dislike_post'),
]
