from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tutorial(models.Model):
    tutorial_uploader = models.ForeignKey(User , on_delete=models.CASCADE)
    tutorial_title = models.TextField(blank=True)
    tutorial_description = models.TextField(blank=True)
    tutorial_tags = models.TextField(blank=True)
    tutorial_video = models.FileField(upload_to='videos')
    tutorial_like = models.ManyToManyField(User , blank=True , related_name='tutorial_likes')
    timestamp = models.DateField(auto_now_add=True)