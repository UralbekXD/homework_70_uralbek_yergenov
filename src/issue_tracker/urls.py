from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),


    # Tasks
    path('tasks/', IndexView.as_view(), name='tasks'),
    path('tasks/task/create/', TaskAddView.as_view(), name='task_create'),
    path('tasks/task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/task/edit/<int:pk>/', TaskEditView.as_view(), name='task_update'),
    path('tasks/task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),


    # Projects
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/project/create/', ProjectAddView.as_view(), name='project_create'),
    path('projects/project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),

    # Add Task to Project
    path('projects/project/<int:pk>/task/create', ProjectTaskAddView.as_view(), name='project_task_create'),

]
