from django.urls import path
from . import views
app_name='myapp'

urlpatterns=[
    path('', views.index_page,name="index"),
    path('about/',views.about_us,name="about"),
    path('story/',views.our_story,name="story"),
    path('contact/',views.contact_us,name="contact"),
]