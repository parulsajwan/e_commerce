# ###
# URL patterns for Orders
# ###

from django.urls import path, include
from rest_framework import routers

from ecom.views.OrderView import OrderViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)

# for  Orders
urlpatterns = [
    path('', include(router.urls))
]
