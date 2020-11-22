from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.photo,name='photo'),
    path('search/', views.search_profile, name='search_profile'),
    path('profile/',views.profile, name='photo'),
    path('new_post/', views.new_post,name ='new_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)