from django.db import models
import pathlib
from django.db.models.fields.related import ForeignKey
from datetime import datetime
from django.forms import widgets
from django.http import request
from django.utils.text import slugify
from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from multiselectfield import MultiSelectField
from django.urls import reverse
from django.conf import settings
from blog.models import Auto_Reply

User = settings.AUTH_USER_MODEL
# Create your models here.
class datebaseTickets(models.Model):
    db = models.CharField(max_length=100,verbose_name='Database Name',blank=True,null=True)
    user = models.ForeignKey(User ,null=True, on_delete=models.CASCADE, blank=True)
    class Meta:
        verbose_name = ("datebaseTicket")
        verbose_name_plural = ("datebaseTickets")

    def __str__(self):
        return self.db

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

def image_upload_handler(instance,filename):
    #fpath = pathlib.Path(filename)

    return f'user_{instance.user}/{filename}'
    

class Ticket(models.Model):
    dbRelated = models.ForeignKey(datebaseTickets,null=True, on_delete=models.CASCADE, blank=True,verbose_name='Database')
    # user = models.ForeignKey("auth.User", null=True, blank=True,on_delete=models.SET_NULL)
    user = models.ForeignKey(User ,null=True, on_delete=models.CASCADE, blank=True)
    issueTitle = models.CharField(max_length=100,verbose_name='issue Title')
    issueContent = models.TextField(verbose_name='issue content')
    snapShot = models.ImageField(
        upload_to=image_upload_handler, default="default.png",null=True, blank=True)
    
    status =  models.CharField(
        choices=[("Open","Open"),("Closed","Closed"),("Done","Done"),("Waiting","Waiting reply")], max_length=50, null=True, blank=True,default='Open',)
   
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name="Time added", null=True, blank=True)
    updates = models.DateTimeField(auto_now=True,verbose_name="Last Updated", null=True, blank=True)
    def __str__(self):
        return self.issueTitle
    def get_absolute_url(self):
        return reverse("ticketdetails",kwargs={"id":self.id})
    def get_update_url(self):
        return reverse("ticketupdate",kwargs={"id":self.id})
    def get_replys(self):
        return self.ticket_reply_set.all()
    def get_auto_replys(self):
        return self.ai_reply_set.all()
 
class Ai_Reply(models.Model):
    aiReply = models.ForeignKey(Auto_Reply, on_delete=models.CASCADE, blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, blank=True)
    
    def get_absolute_url(self):
        return self.ticket.get_absolute_url()
    

class Ticket_reply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    author = models.ForeignKey(User ,null=True, on_delete=models.CASCADE)
    reply = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True ,verbose_name="Time added")
    
    
    def get_absolute_url(self):
        return self.ticket.get_absolute_url()
            
        
    

    
# Create your models here.
class Contact1(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=50,verbose_name='Phone number',null=True,blank=True)
    company = models.CharField(max_length=100,verbose_name='company',null=True,blank=True)
    notes = models.CharField(max_length=200,null=True,blank=True)
    subject = models.TextField(blank=True)
    data = models.DateTimeField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name 


# class QuickBook(models.Model):
#     email = models.EmailField(verbose_name="Email")
#     mainService = models.CharField(max_length=100,verbose_name="Main")
#     moreServices= SelectMultiple()


class Booking(models.Model):
    MY_CHOICES = (('ODOO DEVELOPMENT', 'ODOO DEVELOPMENT'),
              ('CODE UPGRADING', 'CODE UPGRADING'),
              ('DATABASE MIGRATION', 'DATABASE MIGRATION'),
              ('LINUX ADMINISTRATION', 'LINUX ADMINISTRATION'),
              )

    email = models.EmailField(verbose_name="Email")
    mainService = models.CharField(max_length=100,verbose_name="Main")
    my_field = MultiSelectField(choices=MY_CHOICES,max_choices=3)
    SpecialOrder = models.CharField(max_length=100,verbose_name="Special",default='None',null=True,blank=True)
    
    def __str__(self):
            return self.email
