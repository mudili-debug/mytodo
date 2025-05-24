from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)  # Task title up to 100 characters
    completed = models.BooleanField(default=False)  # Task completion status, defaults to False

    def __str__(self):
        return self.title  # Return task title as string representation
