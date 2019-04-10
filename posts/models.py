from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=150)
    
    def __str__(self):
        return f"포스트 내용 : {self.content}"
