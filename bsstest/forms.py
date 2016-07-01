from django import forms



from .models import *
from django.contrib.auth.models import User
 
class bsstestForm(forms.ModelForm):
    class Meta:
        model = bsstest 
   	fields = ('name','username','password','firstname','lastname','mobilenumber')




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


		
