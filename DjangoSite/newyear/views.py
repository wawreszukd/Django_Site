from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    time = datetime.datetime.now()
    if(time.day==1 and time.month==1):
        context = {
            "newyear": "Yes"
            }
    elif(time.day==14 and time.month==1):
        context = {
            "newyear": "Yes but orthodox"
        }
    else:
        context= {
            "newyear": "No"
        }
    return render(request,"newyear/index.html",context=context)
    