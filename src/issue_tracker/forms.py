from django import forms
from django.core.validators import BaseValidator, ValidationError

from .models import Task, Type, Status, Project


class MinimumLengthValidator(BaseValidator):
    def __init__(self, min_value):
        message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
        super().__init__(limit_value=min_value, message=message)

    def compare(self, value, min_value):
        return value < min_value

    def clean(self, value):
        return len(value)


class MaximumLengthValidator(BaseValidator):
    def __init__(self, max_value=20):
        message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
        super().__init__(limit_value=max_value, message=message)

    def compare(self, value, max_value):
        return value > max_value

    def clean(self, value):
        return len(value)


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=256,
        required=False,
        label='Найти',
    )


class TaskForm(forms.ModelForm):
    short_description = forms.CharField(
        validators=(MinimumLengthValidator(min_value=2), MaximumLengthValidator(max_value=128)),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3'
            }
        )
    )

    class Meta:
        model = Task
        fields = [
            'short_description',
            'full_description',
            'statuses',
            'types',
            'project',
        ]

        labels = {
            'short_description': 'Краткое описание',
            'full_description': 'Полное описание',
            'statuses': 'Статусы',
            'types': 'Типы',
        }

        widgets = {
            'full_description': forms.Textarea(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'statuses': forms.SelectMultiple(
                attrs={
                    'class': 'form-select mb-3'
                },
                choices=Status.objects.all(),
            ),
            'types': forms.SelectMultiple(
                attrs={
                    'class': 'form-select mb-3'
                },
                choices=Type.objects.all()
            ),
            'project': forms.Select(
                attrs={
                    'class': 'form-select mb-3'
                },
            ),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'start_date',
            'end_date',
        ]

        labels = {
            'name': 'Название',
            'full_description': 'Описание',
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-select mb-3'
                },
            ),
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control mb-3'
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control mb-3'
                }
            ),
        }


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'short_description',
            'full_description',
            'statuses',
            'types',
        ]

        labels = {
            'short_description': 'Краткое описание',
            'full_description': 'Полное описание',
            'statuses': 'Статусы',
            'types': 'Типы',
        }

        widgets = {
            'short_description': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'full_description': forms.Textarea(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'statuses': forms.SelectMultiple(
                attrs={
                    'class': 'form-select mb-3'
                },
                choices=Status.objects.all(),
            ),
            'types': forms.SelectMultiple(
                attrs={
                    'class': 'form-select mb-3'
                },
                choices=Type.objects.all()
            ),
        }

