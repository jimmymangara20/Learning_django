from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request,"index.html")

def about_us(request):
    return render(request,"about.html")

def our_story(request):
    return render(request,"story.html")

def contact_us(request):
    return render(request,"contact.html")