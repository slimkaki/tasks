from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser



# Create your views here.

# seguindo o tutorial: https://www.askpython.com/django/django-listview
@csrf_exempt
def index(request):
    if request.method == 'GET':
        all_tasks = Task.objects.values()
        serializer = TaskSerializer(all_tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer = TaskSerializer(data=request)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    return HttpResponse("Hello, world. You're at the tasks index.")
