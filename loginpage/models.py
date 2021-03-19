from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     description = models.CharField(max_length=400,blank=True)
     is_mentor = models.BooleanField(default=False , blank=True)