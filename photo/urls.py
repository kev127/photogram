from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.login,name='photo'),
    path('search/', views.search_profile, name='search_profile'),
    path('profile/',views.profile, name='profile'),
    path('new_post/', views.new_post,name ='new_post'),
    path('login/', views.login,name ='login'),
    path('accounts/register/', views.register, name='register'),
    path('update_profile/',views.update_profile,name = 'update_profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)