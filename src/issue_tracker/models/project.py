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

    def __str__(self):
        return self.name
