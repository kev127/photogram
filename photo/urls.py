from django.urls import path
from . import views

urlpatterns=[
    path('',views.photo,name='photo'),
     path('search/', views.search_profile, name='search_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)