from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UserModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
"""
1. 로그인 폼을 만든다.
    -> 이건 user데이터베이스를 상속해서 만들어야할듯?
        -> bootstrap 나중에 넣기.
2. 인증을 받는다.
3. 로그인한다.
"""

# Create your views here.
def login(request):
    if request.method == "POST":
        # form = UserModelForm(request.POST)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
        else:
            return redirect('accounts:login')
    else:
        # form = UserModelForm()
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {
            'form' : form
        })
    
    
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth_login(request, form.instance)
            # 여기서는 get_user 못씀!
            return redirect('posts:list')
        else:
            return redirect('accounts:signup')
        
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {
            'form' : form
        })
    