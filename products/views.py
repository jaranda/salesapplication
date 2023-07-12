from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config.pagination import CustomPagination
from products.models import Product
from products.serializers import ProductSerializer
from users.authentication import JWTAuthentication


class ProductGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })

        return self.list(request)    

    def post(self, request):
        request.data.update({
            'password': 1234,
            'role': request.data['role_id']
        })
        return Response({
            'data': self.create(request).data
        })
    
    def put(self, request, pk=None):
        if(request.data['role_id']):
            request.data.update({
                'role': request.data['role_id']
            })
        
        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

