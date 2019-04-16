from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    
    def __str__(self):
        return f"포스트 내용 : {self.content}"

class Comment(models.Model):
    content = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
"""
Model 자투리 시간에 공부하기

1. Field options
    - null : django will store empty value as NULL in the DB
        (database-related)
    - blank : this field is allowed to be blank. 
        (validation-related) 
        => so, form validation will allow entry of an empty value.
    - choices : An iterable of 2-tuples
        => default form widget will be a select box
        ex)
            SHIRT_SIZES = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
                ) => 
        the select option 'Small' will be stored in DB as 'S'
"""
