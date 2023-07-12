from django.urls import path

from users.views import login, register, users

urlpatterns = [
    path('users/', users),
    path('register/', register),
    path('login/', login)
]