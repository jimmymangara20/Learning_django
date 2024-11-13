from django.urls import path

app_name='templating'

from.import views

urlpatterns=[
    path('',views.home,name="landing_page"),#url for the landing page
    path('about/',views.about_us,name="about"),
    path('contact/',views.contact_us,name="contact"),
    path('team/',views.our_team,name="team"),
    path('story/',views.our_story,name="story"),
]