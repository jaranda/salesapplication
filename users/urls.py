from django.urls import path

from users.views import (
    AuthenticatedUser,
    PermissionAPIView,
    ProfileInfoAPIView,
    ProfilePasswordAPIView,
    RoleViewSet,
    UserGenericAPIView,
    login,
    logout,
    register,
)

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('user/', AuthenticatedUser.as_view()),
    path('logout/', logout),
    path('permissions/', PermissionAPIView.as_view()),
    path('roles/', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users/info', ProfileInfoAPIView.as_view()),
    path('users/password', ProfilePasswordAPIView.as_view()),
    path('users/', UserGenericAPIView.as_view()),
    path('users/<str:pk>', UserGenericAPIView.as_view())
]