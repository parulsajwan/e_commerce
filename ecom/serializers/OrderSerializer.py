
from rest_framework import serializers
from ecom.models import (
    Order
)
from . import SnippetSerializer as snip

class OrderDetailsSerializer(serializers.ModelSerializer):
    product = snip.ProductDetailSerializer()
    user = snip.UserDetailSerializer()
    class Meta:
        model = Order
        fields = ('id', 'product', 'user')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
