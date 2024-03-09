from django import forms
from .models import Task

class TaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'task_assign_date': forms.DateInput(attrs={'type': 'date'})
        }