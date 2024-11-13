from django.contrib import admin
from django.urls import  path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Registering my app urls
    path('installation/', include('learning_app.urls', namespace='main')),
    path('',include('templating.urls')),
    
]

