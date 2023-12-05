from django.urls import path
from . import views

urlpatterns = [
    path('create-project', views.ProjectCreateView.as_view(), name ='create-project'),
    path('projects', views.projects, name = 'projects'),
    path('home', views.home, name = 'home'),
    path('projects/<int:pk>', views.projectDetail, name ='project-detail'),
    path('tasks', views.taskList, name ='tasks'),
    path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),
    path('create-task', views.taskCreate, name ='create-task'),
    path('update-task/<int:pk>', views.TaskUpdateView.as_view(), name ='update-task'),
    path('update-project/<int:pk>', views.ProjectUpdateView.as_view(), name ='update-project'),
    path('delete-task/<int:pk>', views.TaskDeleteView.as_view(), name ='delete-task'), 
path('delete-project/<int:pk>', views.ProjectDeleteView.as_view(), name ='delete-project'),
path('join-task/<int:pk>', views.joinTask, name ='join-task'),
]

