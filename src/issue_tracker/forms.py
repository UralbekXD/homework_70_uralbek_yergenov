from django import forms

from .models import Task, Type, Status


class TaskForm(forms.ModelForm):
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
            )
        }
