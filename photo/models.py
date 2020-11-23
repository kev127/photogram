from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django import forms
from django.db import models
from cloudinary.models import CloudinaryField

import cloudinary

# Create your models here.
class Image(models.Model):
    profile_pic = CloudinaryField('image')
    image_name = models.CharField(max_length=40)
    image_caption = HTMLField() 
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0,blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = CloudinaryField('image')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)

    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()

    
    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile_name=value)

   
    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model):
    profile_pic = CloudinaryField('image')
    title = models.CharField(max_length=30, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    caption = models.TextField(max_length=300)

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def update_post(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all.count()

