from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileModelForm, CustomUserCreationForm
from .models import Profile

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            # 여기서는 get_user 못씀!
            return redirect('accounts:update')
        else:
            return redirect('accounts:signup')
        
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {
            'form' : form
        })

def people(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # 1. settings.AUTH_USER_MODEL (django.conf) -> 얘는 view에서 못쓴다고함.
    # 2. get_user_model() (django.contrib.auth import get_user_model())
    return render(request, 'accounts/people.html', {
        'person':person,
    })

@login_required
def update(request):
    """
    지금 있는 정보를 보여줌
    사용자들에게 정보를 받아서 db에 반영함.
    """
    user_profile, created = Profile.objects.get_or_create(
        user = request.user
    )
    
    # if hasattr(request.user, 'profile'):
    #     instance = request.user.profile
    # else:
    #     instance = Profile.objects.create(user=request.user)
    
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileModelForm(request.POST, instance=user_profile)
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile = profile_form.save()
            return redirect('people', user.username)
        else:
            return redirect('accounts:update')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileModelForm(instance=user_profile)
        #PasswordChangeForm은 첫번째인자로 request.user를 받기 때문에 instance라고 명시하면 안됨..
        context = {
            'user_change_form' : user_change_form,
            'profile_form' : profile_form,
        }
        return render(request, 'accounts/update.html', context)

@login_required
def delete(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('accounts:signup')
    else:
        return render(request, 'accounts/delete.html')
        
def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
        return redirect('people', user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
        return render(request, 'accounts/password.html', {
            'password_change_form' : password_change_form
        })

def follow(request, user_id):
    to_user = get_object_or_404(get_user_model(), pk=user_id)
    from_user = request.user
    
    if to_user in from_user.following.all():
        from_user.following.remove(to_user)
    else:
        from_user.following.add(to_user)
    
    return redirect('people', to_user)

