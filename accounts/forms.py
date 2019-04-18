from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name',]


""" 
UserCreationForm 클래스가
기본적으로 meta를 auth에서 정의된 User를 사용하기 때문에

그것을 커스터마이징한 유저모델로 바꿔주는걸 추천함
"""
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields
        


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname','image']
