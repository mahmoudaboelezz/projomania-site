from django import forms
from django.forms import fields
from django.http import request
from .models import Contact1,Booking,Ticket,Ticket_reply,datebaseTickets
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactUs(forms.ModelForm):
    class Meta:
        model = Contact1
        fields = '__all__'
        exclude = ('data',)

        """ widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        } """
"""        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        } """
        
        
class Services(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
    

class Tickets(forms.ModelForm):
    required_css_class = 'require-field'
    class Meta:
        model = Ticket
        fields = '__all__'
        # fields = [ 'issueTitle','issueContent','status']
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['snapShot'].id="lolwell"
        
        self.fields['snapShot'].widget.attrs.update({'class':'test','rows':"30"})
        print(self.fields['snapShot'])
    
class Tickets_reply(forms.ModelForm):
    class Meta:
        model = Ticket_reply
        fields = '__all__'
    
class datebaseTickets_Form(forms.ModelForm):
    class Meta:
        model = datebaseTickets
        fields = ['db']
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['db'].queryset = datebaseTickets.objects.filter(
    #         pk = user.id)