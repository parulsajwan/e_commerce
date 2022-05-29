from rest_framework import viewsets,status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from ecom.models.Order import Order
from ecom.serializers.OrderSerializer import (
    OrderSerializer, 
    OrderDetailsSerializer
)

@method_decorator(csrf_exempt, name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return OrderSerializer
        return OrderDetailsSerializer