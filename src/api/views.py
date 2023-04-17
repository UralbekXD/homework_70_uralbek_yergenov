from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import ProjectSerializer, TaskSerializer
from issue_tracker.models import Project, Task, Status, Type


class ProjectListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return Response(projects_serializer.data, status=status.HTTP_200_OK)


class ProjectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        project_serializer = ProjectSerializer(project)
        return Response(project_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        project_serializer = ProjectSerializer(project, data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task = Task.objects.all()
        task_serializer = TaskSerializer(task, many=True)
        return Response(task_serializer.data, status=status.HTTP_200_OK)


class TaskAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task_serializer = TaskSerializer(task, data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
