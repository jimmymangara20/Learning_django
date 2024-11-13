#Import path from django.urls
#You register app urls to project urls
from django.urls import path

from . import views

app_name = 'main'

urlpatterns= [
    path('',views.welcome_home,name="home"), #home url
    path('about/',views.about_us,name="about"), #about us url
    path('story/',views.our_story,name="story"),
    path('team/',views.our_team,name="team"),
    path('contact/',views.contact_us,name="contact"),
    
    
]