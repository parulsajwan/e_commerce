from django.shortcuts import render
from rest_framework import viewsets
from ecom.models.Order import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ecom.serializers.OrderSerializer import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
