#utilizaremos modulos 
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent h-32',
                'placeholder': 'Enter task description'
            }),
            'important': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-purple-600 border-gray-300 rounded focus:ring-purple-500'
            })
        }
