from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, TemplateView, UpdateView, DeleteView

from issue_tracker.models import Task, Type, Status
from issue_tracker.forms import TaskForm


class TaskDetailView(TemplateView):
    template_name = 'issue_tracker/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=context.get('pk'))
        return context


class TaskAddView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'issue_tracker/task_create.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if not form.is_valid():
            return render(request, 'issue_tracker/task_create.html', context={
                'form': form,
            })

        task = Task.objects.create(
            short_description=form.cleaned_data.get('short_description'),
            full_description=form.cleaned_data.get('full_description'),
        )

        statuses = form.cleaned_data.get('statuses')
        for status in statuses:
            task.statuses.add(
                Status.objects.get(name=status)
            )

        types = form.cleaned_data.get('types')
        for type in types:
            task.types.add(
                Type.objects.get(name=type)
            )

        return redirect('index')


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'issue_tracker/task_update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('tasks')

