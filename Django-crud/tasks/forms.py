#utilizaremos modulos 
from django.forms import ModelForm
from .models import Task  # Cambiar tasks por Task

class TaskForm(ModelForm):  # Cambiar a PascalCase para seguir convenciones
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']  # Corregir 'tilte' a 'title'
