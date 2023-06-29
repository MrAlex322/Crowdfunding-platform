from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('create_news_post/', views.create_news_post, name='create_news_post'),
    path('edit_news_post/<slug:slug>/', views.edit_news_post, name='edit_news_post'),
    path('<slug:slug>/', views.view_news_post, name='view_news_post'),
    path('like/<int:pk>/', views.add_like, name='add_like'),
    path('dislike/<int:pk>/', views.add_dislike, name='add_dislike'),
]

