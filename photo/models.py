from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'photo/' ,null=True)
    image_name = models.CharField(max_length=40)
    image_caption = HTMLField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0,blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
