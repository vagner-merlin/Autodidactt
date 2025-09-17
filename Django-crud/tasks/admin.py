from django.contrib import admin
from .models import tasks

# Register your models here.

class taskadmin(admin.ModelAdmin):
    readonly_fields = ('created',) #campo de solo lectura para que no se pueda modificar la fecha de creacion
    

admin.site.register(tasks , taskadmin) #registra el modelo tasks en el admin para poder gestionarlo desde la interfaz de admin 