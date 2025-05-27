from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "gp_web/index.html")

def gallery(request):
    return render(gallery, "gp_web/gallery.html")

def about(request):
    return render(request, "gp_web/about.html")

def contact(request):
    return render(contact, "gp_web/contact.html")

def error(request):
    return render(error, "gp_web/error.html")