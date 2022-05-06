from pydoc import describe
from turtle import title
from django.db import models


# Create your models here.
status_choices = (
    ('In Progress', 'In Progress'),
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
)


class Todolist(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    do_date = models.DateTimeField()
    status = models.CharField(default='In Progress', choices=status_choices,max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)