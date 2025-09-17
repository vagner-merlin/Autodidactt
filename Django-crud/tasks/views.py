from django.shortcuts import render, redirect
# para renderizar un formulario de usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# usercraetion para crear un usuario y authenticationform para autenticar un usuario

# me va debolver un formuulario esto que importe
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .forms import taskForm


# Create your views here.
# ejecutar cuando una utl sea visita


# pagina principal
def home(request):
    return render(request, 'home.html')

# registro de usuario


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


@login_required
def tasks(request):
    return render(request, 'tasks/tasks.html', {
        'form': taskForm()
    })


def logout_view(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')


def create_task(request):
    if request.method == 'GET':
            return render(request, 'tasks/create_tasks.html', {
            'form': taskForm()
        })
    else:
        form = taskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('tasks')
