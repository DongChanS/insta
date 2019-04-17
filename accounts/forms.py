from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name',]

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname']