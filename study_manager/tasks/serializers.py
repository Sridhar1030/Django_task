from rest_framework import serializers
from .models import Task, PomodoroSession

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task', 'completed', 'created_at', 'duration', 'task_type']  # Include all fields

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = '__all__'
