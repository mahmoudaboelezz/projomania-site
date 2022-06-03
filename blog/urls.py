from django.urls import path
from .views import Articles,Articledetail,viewsets_erros
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests',viewsets_erros)

urlpatterns = [
    path('blogs/', Articles, name='articles'),
    path('blogs/<slug:slug>/', Articledetail, name='articledetail'),
    path('django/viewsets/',include(router.urls)),
] 