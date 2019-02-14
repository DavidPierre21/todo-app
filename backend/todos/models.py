from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner')

    contributors = models.ManyToManyField(
        User,
        default=None,
        related_name='contributions')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    responsible = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='tasks')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title
