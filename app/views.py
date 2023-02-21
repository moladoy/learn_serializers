from rest_framework.viewsets import ModelViewSet

from app.models import Product
from app.serializers import ProductSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
