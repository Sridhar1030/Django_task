from django.urls import path
from .views import index, task_manager, pomodoro_manager, new_task_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('task.html', task_manager, name='task_manager'),  # Task manager page
    path('pomodoro.html', pomodoro_manager, name='pomodoro'),  # Pomodoro page
    path('task/new/', new_task_view, name='new_task'),  # Route for creating a new task
]
