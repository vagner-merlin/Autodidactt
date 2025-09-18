from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):  # Debe ser Task en singular, no tasks
    title = models.CharField(max_length=200)  # Corregir si está como 'tilte'
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # muestra el titulo y el usuario al que pertenece la tarea