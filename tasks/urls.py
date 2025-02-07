from django.urls import path
from . import views
from .views import task_list, task_detail, task_create, task_update, task_delete, task_complete  # Certifique-se de importar task_complete

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('new/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/complete/', task_complete, name='task_complete'),  # Certifique-se de que essa linha existe
]
