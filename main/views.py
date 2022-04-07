from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Task
from main.serializers import TaskListSerializer, TaskDetailSerializer


def get_todo_list(request):
    tasks = Task.objects.all()
    return render(request,
                  'main/todo_list.html',
                  {'title': 'TODO List',
                   'tasks': tasks,
                   'completed': False})


def get_completed_todo_list(request, id):
    tasks = Task.objects.filter(id=id)
    return render(request,
                  'main/completed_todo_list.html',
                  {'title': 'Completed TODO List',
                   'tasks': tasks,
                   'completed': True})


@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        books = Task.objects.all()
        serializer = TaskListSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TaskListAPIView(APIView):

    def get(self, request):
        books = Task.objects.all()
        serializer = TaskListSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):

    def get(self, request, id):
        books = Task.objects.filter(id=id).first()
        serializer = TaskDetailSerializer(books)
        return Response(serializer.data)
