from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Task
from .serializers import TaskSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def index(request):
    return HttpResponse("Available endpoints:</br>/get_all</br>/get_single/{id_task}</br>/post</br>/delete/{id_task}</br>/update/{id_task}")

@api_view(["GET"])
def get_all_tasks(request):
    all_tasks = Task.objects.values()
    serializer = TaskSerializer(all_tasks, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def get_single_task(request, id_task):
    try:
        task = Task.objects.get()
        serializer = TaskSerializer(task, many=True)
    except:
        raise Http404("Não achei a task especificada!")
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def post_task(request):
    data=JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=401)


@api_view(["DELETE"])
def delete_task(request, id_task):
    try:
        task = Task.objects.get(pk=id_task)
        task.delete()
    except:
        raise Http404("Não achei a task especificada!")
    return HttpResponse("Deletado com sucesso!", status=201)

@api_view(["PATCH"])
def update_task(request, id_task):
    try:
        task = Task.objects.get(pk=id_task)

    except:
        raise Http404("Não achei a task especificada!")
    return HttpResponse("Task alterada com sucesso!", status=201)

