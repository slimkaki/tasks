from rest_framewoork import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = ['title', 'pub_date', 'description']