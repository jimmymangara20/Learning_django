from django.shortcuts import render

# Create your views here.
def home(request):
    """Display the home page"""
    context={}
    return render(request,"templating/home.html",context)

def about_us(request):
    context={}
    return render (request,"templating/about.html",context)

def contact_us(request):
    context={}
    return render(request,"templating/contact.html",context)

def our_team(request):
    context={}
    return render (request,"templating/our_team.html",context)

def our_story(request):
    context={}
    return render (request,"templating/story.html",context)
    