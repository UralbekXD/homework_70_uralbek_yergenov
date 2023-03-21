from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    start_date = models.DateField(
        null=False,
        blank=False,
        verbose_name='Дата начала'
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата окончания'
    )

    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Название',
    )

    description = models.TextField(
        max_length=4096,
        null=False,
        blank=False,
        verbose_name='Описание',
    )

    users = models.ManyToManyField(
        User,
        blank=True,
        related_name='projects',
        verbose_name='Пользователи',
    )

    class Meta:
        permissions = [
            ('create_project_users', 'Создовать пользователей проекта'),
            ('delete_project_users', 'Удалять пользователей проекта'),
        ]

    def __str__(self):
        return self.name
