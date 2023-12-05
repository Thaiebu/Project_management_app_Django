from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import datetime
from django.views.generic import ListView
from django.views.generic.edit import CreateView , UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Case, When, Value
from .models import Project,Task


# Create your views here.

def home(request):
    return render(request, 'index.html')
# def current_time(request):
#     current_date_time = datetime.datetime.now()
#     return HttpResponse(f"The Current time: {current_date_time}")

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',context)

def projectDetail(request,pk):
    project = get_object_or_404(Project, id=pk)
    project_tasks = project.task_set.all()

    context = {'project':project,'project_tasks':project_tasks}
    return render(request, 'projects/project-detail.html',context)

def taskList(request):
    user_tasks =Task.objects.filter(assignee=request.user).order_by(
        Case(
        When(status='TO DO', then=Value(1)),
        When(status='IN-PROGRESS', then=Value(2)),
        When(status='COMPLETED', then=Value(3)),
        default=Value(4),
    ),'due_date')
    tasks = Task.objects.filter(assignee=None)
    context = {'tasks':tasks,'user_tasks':user_tasks}
    return render(request, 'projects/tasks.html',context)

def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'projects/task-detail.html',context)

from .forms import TaskForm

def taskCreate(request):
   form = TaskForm
   if request.method == "POST":
       form =TaskForm(request.POST)
       if form.is_valid():
           form.save() 
           return redirect('tasks')  

   context = {'form':form}
   return render(request, 'projects/task-create.html',context)

# class TaskListView(ListView):
#    model = Task
#    #print(model)
# #    for m,n in model.objects.all():
# #        print(m,n)
#    template_name = 'projects/tasks.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'projects/project_create_form.html'

class ProjectCreateView(CreateView):
   model = Project
   fields = ["name","description"]
   template_name = 'projects/project_create_form.html'
   success_url = reverse_lazy('projects')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update_form.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'projects/task_update_form.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'projects/task_confirm_delete.html'
 
    
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'


def joinTask(request,pk):
   task =Task.objects.get(id=pk)
   task.assignee=request.user
   task.save()
   return redirect('tasks')