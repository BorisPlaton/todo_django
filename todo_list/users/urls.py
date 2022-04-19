from django.urls import path, include
import django.contrib.auth.urls

from users.views import login_user, register_user

app_name = 'users'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login')
]