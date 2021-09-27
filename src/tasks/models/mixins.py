from django.db import models


class TimeStampMixin(models.Model):
    created = models.DateTimeField(
        'Created',
        auto_now_add=True,
        editable=False,
    )
    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True
