from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms


# Create your views here.


class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    models = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')


class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    success_url = reverse_lazy('Project_list')

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])


class ProjectDeleteView(DeleteView):
    models = models.Task
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')


class TaskCreateView(CreateView):
    models = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    models = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    models = models.Task

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


