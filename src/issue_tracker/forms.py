from django import forms
from django.core.validators import BaseValidator, ValidationError

from .models import Task, Type, Status


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

    def clean_short_description(self):
        short_description = self.cleaned_data.get('short_description')
        tasks = Task.objects.filter(short_description=short_description)
        if len(tasks) >= 1:
            raise ValidationError('Short description like this, already exist!')

        return short_description
