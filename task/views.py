from django.shortcuts import render, redirect
from .forms import TaskFrom
from .models import Task

def add_task(request):
    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_tasks")

    form = TaskFrom()
    return render(request, "add_task.html", {'form': form})

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def edit_task(request, id):
    try :
        task = Task.objects.get(pk = id)
        form = TaskFrom(instance=task)
        if request.method == 'POST':
            form = TaskFrom(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("show_tasks")

        return render(request, 'edit_task.html', {'form': form})
    except:
        return redirect("show_tasks")
    
def complete_task(request, id):
    try :
        task = Task.objects.get(pk = id)
        task.is_completed = True
        task.save()
    finally:
        return redirect("show_tasks")

def delete_task(request, id):
    try :
        task = Task.objects.get(pk = id)
        task.delete()
    finally:
        return redirect("show_tasks")