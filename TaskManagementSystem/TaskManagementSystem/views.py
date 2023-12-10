from django.shortcuts import render
from task.models import TaskModel

def base(request):
    return render(request, 'base.html')

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})