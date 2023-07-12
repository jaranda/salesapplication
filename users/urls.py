from django.urls import path

from users.views import AuthenticatedUser, PermissionAPIView, login, logout, register

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('user/', AuthenticatedUser.as_view()),
    path('logout/', logout),
    path('permissions/', PermissionAPIView.as_view())
]