from django import forms
from django.conf import settings
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    
    class Meta:
        # model = settings.AUTH_USER_MODEL
        model = User
        fields = ['username','password']
        
        widgets = {
            'password' : forms.PasswordInput()
        }