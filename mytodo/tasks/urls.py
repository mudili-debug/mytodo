from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views

app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    # Web views
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),       # corrected function name
    path('update/<int:task_id>/', views.task_update, name='task_update'),  # corrected function name
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),  # corrected function name
    path('weather/', views.weather_view, name='weather'),

    # API endpoints
    path('api/', include(router.urls)),
]
