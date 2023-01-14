from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(f"Hello, world!<br> You can add your name after / to interact with website")
def hello(request, name):
    context = {
        "name": name
    }
    return render(request,"hello/index.html",context)