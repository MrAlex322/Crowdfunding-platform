from django.urls import path, include
from users.views import Register, news_list
from . import views

urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
    path('news/', views.news_list, name='news_list'),
    path('register/', Register.as_view(), name='register'),
    path('create_news_post/', views.create_news_post, name='create_news_post'),
]