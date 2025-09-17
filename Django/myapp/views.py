from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Project , task
from .forms import create_taskss , create_projectss
from django.shortcuts import get_object_or_404 as get_error_or_404

def about (request):
    return render(request, 'about.html')

def index(request):
    name = "Curso Django"
    return render(request, 'index.html' ,{  
        'name': name
    })
#----------------------------------------------------------------
def projects(request):
    
    Projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': Projects
    })

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': create_projectss()
        })
    else:
        Project.objects.create(
            name=request.POST['name'])
        return redirect('projects')
#----------------------------------------------------------------
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    project_tasks = task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': project_tasks
    })

#----------------------------------------------------------------
def tasks(request):
    tasks = task.objects.all()
    return render(request, 'tasks/tasks.html' , {
        'tasks': tasks

    })
#aqui poodemos modificar para el ingresos de datos a la bd
#no debemos insertar datos con el get solo es para mostrar


def create_tasks(request):
    # Crear una instancia del formulario
    form = create_taskss()
    # Establecer el queryset de proyectos
    form.fields['project'].queryset = Project.objects.all()
    
    if request.method == 'GET':
        return render(request, 'tasks/create_tasks.html', {
            'form': form
        })
    else:
        form = create_taskss(request.POST)
        form.fields['project'].queryset = Project.objects.all()
        
        if form.is_valid():
            task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                project=form.cleaned_data['project']
            )
            return redirect('tasks')
        
        return render(request, 'tasks/create_tasks.html', {
            'form': form
        })    
#este codigo de return redirect lo que hace es debolverete la pagina para que veas es decir como lo dice redirecciona a tasks


#una ruta para retornar la pagian projects
# esta vista recibe un parametro id que es un entero y lo usamos para buscar el proyecto correspondiente en la base de datos 

def project_detail(request ,id):
    project = get_object_or_404(Project, id=id) 
    tasks = task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
        'project': project ,
        'tasks': tasks 
        
    })