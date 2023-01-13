from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip
# Create your views here.

def index(request):
    template = "main/index.html"
    context={
        "trips": Trip.objects.all(),

    }
    return render(request,template,context)