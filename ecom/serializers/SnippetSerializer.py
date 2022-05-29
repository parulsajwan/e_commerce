# ###
# Snippet serializers all go here to prevent circular import problems
# ###
from django.contrib.auth.models import User
from rest_framework import serializers
from ecom.models import (
    Order,
    Product,
    )
class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Product
            fields = ('id','name','description','price')

class UserDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id','username','email')