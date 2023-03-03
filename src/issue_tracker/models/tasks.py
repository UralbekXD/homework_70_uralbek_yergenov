from django.db import models

from ..models import Status, Type


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
    status = models.ManyToManyField(
        Status,
        on_delete=models.RESTRICT,
        related_name='tasks',
        blank=True,
        verbose_name='Статус',
    )

    type = models.ManyToManyField(
        Type,
        on_delete=models.RESTRICT,
        related_name='tasks',
        blank=True,
        verbose_name='Тип',
    )
