from django.urls import path
from . import views

urlpatterns=[
    path('',views.instagram,name = 'instagram'),
    path('',views.photo,name='photo'),
]