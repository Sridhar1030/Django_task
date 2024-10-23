# your_app/views.py
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Task
from django.http import JsonResponse
from .models import PomodoroSession
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def pomodoro_manager(request):
    return render(request, 'tasks/pomodoro.html')
def task_manager(request):
    return render(request, 'tasks/task.html')

def task_form(request):
    if request.method == "POST":
        duration = request.POST.get("duration", 25)  # Default to 25 if not provided
        PomodoroSession.objects.create(duration=duration)
        return JsonResponse({"success": True, "message": "Session saved successfully!"})

    return render(request, 'pomodoro.html')  # Make sure the path is correct



@csrf_exempt  
def new_task_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Load JSON data from the request body
        duration = data.get('duration')  # Get duration from the JSON data
        task_name = data.get('task')  # Get task name from the JSON data
        task_type = data.get('type')  # Get task type (daily/weekly)

        # Create a new task instance and save it to the database
        new_task = Task(task=task_name, duration=duration, task_type=task_type)
        new_task.save()

        return JsonResponse({'message': 'Task created successfully!', 'duration': duration})
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)