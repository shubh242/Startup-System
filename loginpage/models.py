from django.db import models

# Create your models here.
class Client(models.Model):
     username = models.CharField(max_length=70)
     email= models.EmailField(max_length=100)
     password = models.CharField(max_length=100)
     discription = models.CharField(max_length=400,blank=True)
     is_mentor = models.BooleanField(default=False , blank=True)