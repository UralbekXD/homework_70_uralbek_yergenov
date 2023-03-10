from django.views.generic import ListView, DetailView, CreateView

from issue_tracker.models import Project


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
        return context

