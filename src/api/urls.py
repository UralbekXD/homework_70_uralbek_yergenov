from django.urls import path

from .views import ProjectListAPIView, TaskListAPIView, ProjectAPIView, TaskAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('tasks/', TaskListAPIView.as_view()),

    path('project/<int:pk>', ProjectAPIView.as_view()),
    path('task/<int:pk>', TaskAPIView.as_view()),
]
