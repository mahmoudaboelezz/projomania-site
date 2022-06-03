from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('ticket/', views.Ticket_list, name="ticketlist"),
    path('tickets/', views.mylist, name="mylist"),
    path('ticket/create', views.Tickets, name="tickets"),
    path('ticket/<int:id>/update', views.Ticket_update, name="ticketupdate"),
    path('ticket/<int:id>', views.Ticketdetail, name="ticketdetails"), 
    path('contact', views.contactus, name='contactus'),
    path('api-auth/', include('rest_framework.urls')),
    
    
    ]
