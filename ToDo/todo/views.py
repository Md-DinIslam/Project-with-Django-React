from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home_page')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home_page')

def markAsUndone(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = False
    task.save()
    return redirect('home_page')

def editTask(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        task.task = request.POST['updatedTask']
        task.save()
        return redirect('home_page')
    context =  {
        'task' : task,
    }
    return render(request, 'editTask.html', context)

def deleteTask(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    return redirect('home_page')
