from django.shortcuts import render
from django.views.generic import TemplateView

from issue_tracker.models import Task


class IndexView(TemplateView):
    template_name = 'issue_tracker/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

