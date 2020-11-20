from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from .serializers import TaskSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import json

# Create your views here.

@api_view(["GET"])
def index(request):
    return HttpResponse("Available endpoints:</br>/get_all</br>/get_single/{id_task}</br>/post</br>/delete/{id_task}</br>/update/{id_task}</br>/delete_all")

@api_view(["GET"])
def get_all_tasks(request):
    all_tasks = Task.objects.values()
    serializer = TaskSerializer(all_tasks, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["GET"])
def get_single_task(request, id_task):
    try:
        task = Task.objects.get(pk=id_task)
    except:
        return HttpResponse("Não achei a task especificada!", status=404)
    return JsonResponse(model_to_dict(task), status=201, safe=False)

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
        return HttpResponse("Não achei a task especificada!", status=404)
    return HttpResponse("Deletado com sucesso!", status=201)

@api_view(["PUT"])
def update_task(request, id_task):
    try:
        task = Task.objects.get(pk=id_task)
    except:
        return HttpResponse("Não achei a task especificada!", status=404)
    new_task = json.loads(request.body)
    task.update(title=new_task["title"], pub_date=new_task["pub_date"], description=new_task["description"])
    return HttpResponse(serializer.data, status=201)

@api_view(["DELETE"])
def delete_all_tasks(request):
    try:
        Task.objects.all().delete()
    except:
        return HttpResponse("Não foi possível deletar todas as tasks!", status=400)
    return HttpResponse("Todas as tasks fooram deletadas com sucesso!", status=201)