from django.urls import include, path

urlpatterns = [
    path('user/', include('ecom.urls.UserUrls')),
    path('order/', include('ecom.urls.OrderUrls')),
    path('product/', include('ecom.urls.ProductUrls')),
   ]
