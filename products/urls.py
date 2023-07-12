from django.urls import path

from .views import FileUploadView, ProductGenericAPIView

urlpatterns = [
    path('products/', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view()),
    path('upload/', FileUploadView.as_view()),
]
