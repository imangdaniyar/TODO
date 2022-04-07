from rest_framework import serializers

from main.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'task_name',
                  'created_date',
                  'due_to_date')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
