from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Task


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the tasks index.")

def task_list(request):
    context = {'task_list': Task.objects.all()}
    return render(request, 'task/task_list.html', context)

def create_task(request: HttpRequest):
    task=Task(content=request.POST[''])
    task.save()
    return redirect('task/list/')

def delete_task(request, task_id):
    task = Todo.objects.get(id=todo_id)
    task.delete()
    return redirect('task/list/')