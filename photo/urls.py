from django.urls import path
from . import views

urlpatterns=[
    path('',views.photo,name='photo'),
     path('search/', views.search_profile, name='search_profile'),
]