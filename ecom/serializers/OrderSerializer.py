
from rest_framework import serializers
from ecom.models import (
    Order
)
from . import SnippetSerializer as snip

class OrderSerializer(serializers.ModelSerializer):
    product = snip.ProductDetailSerializer()
    user = snip.UserDetailSerializer()
    class Meta:
        model = Order
        fields = ('id', 'product', 'user')
