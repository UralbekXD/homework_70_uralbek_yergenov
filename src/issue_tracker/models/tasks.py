from django.db import models


class Task(models.Model):
    short_description = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Краткое описание',
    )

    full_description = models.CharField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name='Полное описание',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления',
    )

    # Relations
    statuses = models.ManyToManyField(
        to='issue_tracker.Status',
        related_name='tasks',
        blank=True,
        verbose_name='Статус',
    )

    types = models.ManyToManyField(
        to='issue_tracker.Type',
        related_name='tasks',
        blank=True,
        verbose_name='Тип',
    )

    def __str__(self):
        return f'{self.short_description}'
