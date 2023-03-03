from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

from issue_tracker.models import Task, Type, Status
from issue_tracker.forms import TaskForm


class TaskDetailView(TemplateView):
    template_name = 'issue_tracker/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=context.get('pk'))
        return context


class TaskAddView(View):
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


class TaskEditView(TemplateView):
    template_name = 'issue_tracker/task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=context.get('pk'))
        context['form'] = TaskForm(instance=context.get('task'))
        return context

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs.get('pk'))
        form = TaskForm(request.POST, instance=task)

        if not form.is_valid():
            return render(request, 'issue_tracker/task_update.html', context={
                'form': form,
                'task': task,
            })

        form.save()
        return redirect('task_detail', pk=task.pk)


class TaskDeleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs.get('pk'))
        task.delete()

        return redirect('index')

