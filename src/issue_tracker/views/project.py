from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import reverse, get_object_or_404, redirect

from issue_tracker.models import Project, Task
from issue_tracker.forms import ProjectForm, TaskForm, ProjectTaskForm


class ProjectListView(ListView):
    template_name = 'issue_tracker/project_list.html'
    model = Project
    context_object_name = 'projects'
    ordering = ['name']


class ProjectDetailView(DetailView):
    template_name = 'issue_tracker/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at')
        context['tasks'] = tasks
        context['project_task_form'] = ProjectTaskForm()
        return context


class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'issue_tracker/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectEditView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'issue_tracker/project_update.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('projects')


class ProjectTaskAddView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})
