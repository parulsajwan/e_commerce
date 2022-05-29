from django.shortcuts import render
from rest_framework import viewsets
from ecom.models.Product import Product
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from ecom.serializers.ProductSerializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser, IsAuthenticatedOrReadOnly,)