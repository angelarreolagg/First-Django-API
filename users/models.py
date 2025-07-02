from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField()
    username = models.CharField(max_length=80)
    
    def __str__(self):
        return self.username
    
