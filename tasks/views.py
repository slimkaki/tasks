from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



# Create your views here.

# seguindo o tutorial: https://www.askpython.com/django/django-listview

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def getTasks(request, format=None):
    if request.method == 'GET':
        all_tasks = Task.objects.values()
        serializer = TaskSerializer(all_tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def postTask(request, format=None):
    if request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
