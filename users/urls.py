from django.urls import path

from users.views import register, users

urlpatterns = [
    path('users/', users),
    path('register/', register)
]