from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_Complet/', views.tasks_Complet , name='tasks_complet'),
    path('logout/', views.logout_view, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('tasks/create/', views.create_task, name='createT'),
    path('tasks_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks_Complet/<int:task_id>/complete', views.complet_tasks , name='complete_task'),
    path('tasks_Delete/<int:task_id>/complete', views.delete_tasks , name='delete_tasks'),
]
