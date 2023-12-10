from django.shortcuts import render, redirect
from . import forms
from . import models

def add_task(request):
    task_form = forms.TaskForm()
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
        else:
            task_form = forms.TaskForm()

    return render(request, 'task/task.html', {'form1': task_form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')

    return render(request, 'task/task.html', {'form1': task_form})


def detete_task(request, id):
    try:
        task = models.TaskModel.objects.get(pk=id)
        task.delete()
        return redirect('show_tasks')
    except models.TaskModel.DoesNotExist:
        return render(request, 'task/task_not_found.html', {'id': id})