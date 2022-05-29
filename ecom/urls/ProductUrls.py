# ###
# URL patterns for Product
# ###

from django.urls import path, include
from rest_framework import routers

from ecom.views.ProductView import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

# for  Products
urlpatterns = [
    path('', include(router.urls))
]
