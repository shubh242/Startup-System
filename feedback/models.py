from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Feedback(models.Model):
    feedback_uploader = models.ForeignKey(User , on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images',blank=True)
    thoughts = models.TextField(max_length=1000,blank=True)
    question1= models.TextField(max_length=1000,blank=True)
    question2 = models.TextField(max_length=1000,blank=True)
    question3 = models.TextField(max_length=1000,blank=True)
    question4 = models.TextField(max_length=1000,blank=True)

