import uuid

from django.db import models


class DateTimeCustomQuerySet(models.QuerySet):  # noqa
    def get_non_deleted(self) -> models.QuerySet:  # noqa
        return self.filter(
           date_time_deleted__isnull=True
        )


class DateTimeCustom(models.Model):  # noqa
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Идентификатор'
    )
    date_time_created = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )
    date_time_deleted = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        blank=True
    )
    existance_duration = models.DurationField(
        verbose_name='Время существования',
        null=True,
        blank=True,
    )

    class Meta:  # noqa
        abstract = True
