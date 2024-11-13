from django.shortcuts import render

# Create your views here.
def welcome_home(request):
    context={}
    return render(request,"index.html",context)


#About us page
def about_us (request):
    context ={}
    return render(request, "about.html", context)


def  our_story(request):
    context={}
    return render(request,"story.html", context)

def our_team(request):
    context={}
    return render(request,"our_team.html",context)

def contact_us(request):
    context={}
    return render(request,"contact.html",context)

