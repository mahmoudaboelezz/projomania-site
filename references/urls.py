from django.urls import path
from .views import references,Companydetail



urlpatterns = [
    path('references/', references, name='references'),
    path('references/<slug:slug>/', Companydetail, name='companydetail'),
] 