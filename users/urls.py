from django.urls import path

from users.views import AuthenticatedUser, login, register, users

urlpatterns = [
    path('users/', users),
    path('register/', register),
    path('login/', login),
    path('user/', AuthenticatedUser.as_view())
]