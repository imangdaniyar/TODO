from django.contrib import admin

# Register your models here.
from main.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'task_name',
                    'created_date',
                    'due_to_date',
                    'owner',
                    'mark')
    list_filter = ('task_name',
                   'created_date',
                   'due_to_date',
                   'owner',
                   'mark')
    search_fields = ('task_name',)
