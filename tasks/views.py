from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.

# seguindo o tutorial: https://www.askpython.com/django/django-listview
@api_view(["GET"])
def index(request):
    return HttpResponse("Available endpoints:</br>/get</br>/post")

@api_view(["GET"])
def get_tasks(request):
    all_tasks = Task.objects.values()
    serializer = TaskSerializer(all_tasks, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def post_task(request):
    data=JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=401)

