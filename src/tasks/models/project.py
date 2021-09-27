from django.db import models
from django.contrib.auth import get_user_model

from tasks.models.mixins import TimeStampMixin


class Project(TimeStampMixin, models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(
        'Title',
        max_length=255,
    )
    description = models.TextField(
        'Description',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
