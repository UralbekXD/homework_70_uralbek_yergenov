from rest_framework import serializers
from django.contrib.auth import get_user_model

from issue_tracker.models import Project, Task, Status, Type


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']


class TaskSerializer(serializers.ModelSerializer):
    statuses = StatusSerializer(many=True, read_only=True)
    types = TypeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        # Task
        instance.short_description = validated_data.get('short_description')
        instance.full_description = validated_data.get('full_description')
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = ['short_description', 'full_description', 'created_at', 'updated_at', 'statuses', 'types']
        read_only_fields = ['created_at', 'updated_at', 'statuses', 'types']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        # Project
        instance.start_date = validated_data.get('start_date')
        instance.end_date = validated_data.get('end_date')
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.save()
        return instance

    class Meta:
        model = Project
        fields = ['start_date', 'end_date', 'name', 'description', 'users', 'tasks']
        read_only_fields = ['users', 'tasks']
