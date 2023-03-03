from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        verbose_name='Название',
    )
