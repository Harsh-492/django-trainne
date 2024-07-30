from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import MyProject,ProjectModule
from .forms import ProjectForm,ProjectModuleForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView


class CreateProjectView(CreateView):
    model = MyProject
    form_class = ProjectForm
    template_name = 'project/create_project.html'
    success_url = '/project/listproject/'

class ListProjectView(ListView):
    model = MyProject
    template_name = 'project/list_project.html'
    context_object_name = 'projects'

class UpdateProjectView(UpdateView):
    model = MyProject
    form_class = ProjectForm
    template_name = 'project/create_project.html'
    success_url  = '/project/listproject/'

class DeleteProjectView(DeleteView):
    model = MyProject
    context_object_name = 'project'
    template_name  = 'project/delete_project.html'
    success_url = '/project/listproject/'

class CreateProjectModuleView(CreateView):
    model = ProjectModule
    form_class = ProjectModuleForm
    template_name = 'project/create_project.html'
    success_url = '/project/listproject/'
