from django.db import models
from datetime import datetime
from category.models import Category

class Task(models.Model):
    task_title = models.CharField(max_length=255)
    task_description = models.CharField(max_length=2000)
    task_assign_date = models.DateField(default=datetime.now)
    categories = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_title}"