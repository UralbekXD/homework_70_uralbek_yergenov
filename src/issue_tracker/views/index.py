from django.shortcuts import render
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from issue_tracker.models import Task
from issue_tracker.forms import SearchForm


class IndexView(ListView):
    template_name = 'issue_tracker/index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            q1 = Q(short_description__icontains=self.search_value)
            q2 = Q(full_description__icontains=self.search_value)
            query = q1 | q2
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None
