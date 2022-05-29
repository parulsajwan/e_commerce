# ###
# URL patterns for User
# ###

from django.urls import path
from knox import views as knox_views
from ecom.views.UserView import  UserRegisterView, UserLoginView 

#for  User
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    
]