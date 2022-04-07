from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=255)
    created_date = models.DateField()
    due_to_date = models.DateField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    mark = models.BooleanField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
