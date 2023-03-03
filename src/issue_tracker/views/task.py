from django.shortcuts import render
from django.views.generic import TemplateView

from issue_tracker.models import Task


class TaskDetailView(TemplateView):
    template_name = 'issue_tracker/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_primary_key = context['pk']
        context['task'] = Task.objects.get(pk=task_primary_key)
        return context
