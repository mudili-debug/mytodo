from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views

# DRF router for API views
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Web-based task views
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),       # changed from create_task to task_create
    path('update/<int:task_id>/', views.task_update, name='task_update'),  # changed from update_task to task_update
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),  # changed from delete_task to task_delete

    # Weather app view
    path('weather/', views.weather_view, name='weather'),

    # API routes under /api/v1/
    path('api/v1/', include(router.urls)),
]
