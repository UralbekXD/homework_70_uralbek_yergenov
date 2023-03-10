from django.views.generic import ListView, DetailView, CreateView

from issue_tracker.models import Project


class ProjectListView(ListView):
    template_name = 'issue_tracker/project_list.html'
    model = Project
    context_object_name = 'projects'
    ordering = ['name']