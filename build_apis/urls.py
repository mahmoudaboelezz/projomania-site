from django.urls import path
from . import views

app_name='build_apis'
urlpatterns = [
    path('', views.apis_list, name='apis_list'),
    # path('about', views.aboutus, name='aboutus'),
    ]