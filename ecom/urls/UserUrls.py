# ###
# URL patterns for Customer
# ###

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views
from ecom.views.UserView import  UserRegisterView, UserLoginView 

#for  Customer
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    
]