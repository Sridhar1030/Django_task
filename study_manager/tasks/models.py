from django.db import models

class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]

    task = models.TextField(default="taskName")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=0)  # Set a default value
    task_type = models.CharField(max_length=10, choices=TASK_TYPE_CHOICES, default='daily')

    def __str__(self):
        return self.task


class PomodoroSession(models.Model):
    duration = models.IntegerField(default=25)  # default study duration in minutes
    breaks = models.IntegerField(default=5)  # default short break duration in minutes
    long_break = models.IntegerField(default=15)  # default long break duration in minutes

    def __str__(self):
        return f"Session: {self.duration} min study, {self.breaks} min break"
