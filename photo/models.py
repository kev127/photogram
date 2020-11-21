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
    profile_pic = models.ImageField(upload_to='photo/', null='true')
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
