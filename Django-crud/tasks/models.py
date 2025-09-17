from django.db import models
from django.contrib.auth.models import User #importa el modelo de usuario

# Create your models here.
class tasks(models.Model):
    tilte = models.CharField(max_length=200) #texto corto
    description =  models.TextField() #texto mucho mas largo 
    created = models.DateTimeField(auto_now_add=True) #fecha y hora de creacion por defecto  
    datecompletd = models.DateTimeField(null=True) #fecha y hora de completado
    important = models.BooleanField(default=False) #campo boleano verdadero o falso
    user = models.ForeignKey( User , on_delete=models.CASCADE ) #relacion con el usuario es cascade para que si se borra el usuario se borren sus tareas
    def __str__(self):
        return self.tilte + ' - ' + self.user.username #muestra el titulo y el usuario al que pertenece la tarea