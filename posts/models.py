from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return f"포스트 내용 : {self.content}"
        
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
