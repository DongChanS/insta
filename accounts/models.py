from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following")
    
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    image = models.ImageField(blank=True)

    """
    특정 유저.followers : 나를 팔로우 하는 유저들
    
    특정 유저.following : 내가 팔로우하는 유저들
    
    """