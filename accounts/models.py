from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    