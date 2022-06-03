from django.contrib import admin
from django.urls import path, include
from .views import login_view,logout_view,register_view,user_profile


urlpatterns = [    
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('profile/<int:id>', user_profile,name='profile'),
    ]