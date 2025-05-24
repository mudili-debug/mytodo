from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from rest_framework import viewsets, filters
from .serializers import TaskSerializer
import requests

# Django REST Framework ViewSet for API access
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'id']

# Web view to list tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Web view to create a task
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:  # Simple validation to avoid empty titles
            Task.objects.create(title=title, description=description)
            return redirect('task_list')  # Remove 'tasks:' if no namespace is set
        else:
            error = "Title is required."
            return render(request, 'tasks/task_create.html', {'error': error})
    return render(request, 'tasks/task_create.html')

# Web view to update a task
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:
            task.title = title
            task.description = description
            task.save()
            return redirect('task_list')  # Remove 'tasks:' if no namespace is set
        else:
            error = "Title is required."
            return render(request, 'tasks/task_update.html', {'task': task, 'error': error})
    return render(request, 'tasks/task_update.html', {'task': task})

# Web view to delete a task
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Remove 'tasks:' if no namespace is set
    return render(request, 'tasks/task_delete.html', {'task': task})

# Weather App View
def weather_view(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET['city'].strip()
        if city:
            API_KEY = 'your_openweathermap_api_key_here'  # Replace with your actual API key
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            else:
                weather_data = {'error': 'City not found'}
        else:
            weather_data = {'error': 'Please enter a city name'}
    return render(request, 'tasks/weather.html', {'weather': weather_data})
