from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import (
    ProductSerializer,
    StockSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["description", "title"]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        "products",
    ]

    # фильтрация для доп. задания
    search_fields = ["positions__product__title", "positions__product__description"]
