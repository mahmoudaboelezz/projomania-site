from django import forms
from django.forms import fields
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




        
    # def clean(self):
    #     data = self.cleaned_data
    #     title = data.get("title")
    #     qs = Article.objects.filter(title__icontains=title)
    #     if qs.exists():
    #         self.add_error("title", f"\"{title}\" is already in use. Please pick another title.")
    #     return data

        
# print(Services())


# formset = Services()
# print(formset)       

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={             
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={              
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={               
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={               
                "class": "form-control"
            }
        ))
    # slug = forms.CharField()
    

