from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config.pagination import CustomPagination
from products.models import Product
from products.serializers import ProductSerializer
from users.authentication import JWTAuthentication


class OrderGenericAPIView( generics.GenericAPIView, mixins.ListModelMixinn ):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })

        return self.list(request)    