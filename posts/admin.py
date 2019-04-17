from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(get_user_model())




