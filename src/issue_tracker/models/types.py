from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        verbose_name='Назвавние',
    )

    def __str__(self):
        return self.name
