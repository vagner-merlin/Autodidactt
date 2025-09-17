#utilizaremos modulos 
from django.forms import ModelForm
from .models import tasks  # Change Task to tasks to match your model name

class taskForm(ModelForm):
    class Meta:
        model = tasks  # Change Task to tasks
        fields = ['tilte', 'description', 'important']  # Fix typo in 'tilte' to 'title'
