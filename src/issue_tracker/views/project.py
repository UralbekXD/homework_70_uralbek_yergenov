import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.shortcuts import reverse, get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin

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
        users = project.users.all()
        context['tasks'] = tasks
        context['project_task_form'] = ProjectTaskForm()
        context['users'] = users
        return context


class ProjectAddView(PermissionRequiredMixin, CreateView):
    template_name = 'issue_tracker/project_create.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'issue_tracker.add_project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectEditView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'issue_tracker/project_update.html'
    form_class = ProjectForm
    permission_required = 'issue_tracker.change_project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    permission_required = 'issue_tracker.delete_project'

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


class ProjectEditUsersView(LoginRequiredMixin, TemplateView):
    template_name = 'issue_tracker/project_update_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=context.get('pk'))
        project_users = project.users.all()
        context['project'] = project
        context['users'] = User.objects.exclude(username__in=(user.username for user in project_users))
        context['project_users'] = project_users
        return context

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs.get('pk'))

        users_add = request.POST.getlist('users_add')
        if users_add:
            for user_id in users_add:
                user = User.objects.get(pk=user_id)
                project.users.add(user)

        users_remove = request.POST.getlist('users_remove')
        if users_remove:
            for user_id in users_remove:
                user = User.objects.get(pk=user_id)
                project.users.remove(user)

        return redirect('project_detail', pk=project.pk)
