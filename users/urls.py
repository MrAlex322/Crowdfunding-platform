from django.urls import path, include
from users.views import Register
from .views import profile

urlpatterns = [
    path('home/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]