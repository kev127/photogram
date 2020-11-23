from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post,Image
from cloudinary.forms import CloudinaryFileField    
from django.forms import ModelForm    

class ImageForm(ModelForm):
  class Meta:
      model = Image
      fields = '__all__'
  photo = CloudinaryFileField()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['profile_pic', 'bio']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile',]
