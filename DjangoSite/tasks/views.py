from django.shortcuts import render,redirect
from django import forms
from . import models
# Create your views here.
class newTaskForm(forms.Form):
    task = forms.CharField(label="")

def index(request):
    
    tasks = models.Tasks.objects.filter(session= request.session['_auth_user_hash'])
    
    context = {
        "tasks": tasks,
    }
    return render(request,'tasks/index.html',context=context)
def add(request):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            t = models.Tasks(task=task, session=request.session['_auth_user_hash'])
            t.save()
            return redirect('tasks:tasks')
        else:
            return render(request,'tasks/add.html',{
                "form":form
            })
    context = {
        "form": newTaskForm()
    }
    return render(request,'tasks/add.html',context=context)
def update(request, id):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            t = models.Tasks.objects.filter(id=id)
            t.update(task=task)
            return redirect('tasks:tasks')
        return render(request,'tasks/update.html',{
            "form": form
        })
    return render(request, 'tasks/update.html',{
        "form": newTaskForm()
    })
def delete(request,id):
    task = models.Tasks.objects.filter(id=id)
    print(f"{id}")
    task.delete()
    return redirect("tasks:tasks")