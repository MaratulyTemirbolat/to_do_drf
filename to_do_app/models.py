from typing import (
    List,
)

from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet

from abstracts.models import (
    DateTimeCustom,
    DateTimeCustomQuerySet,
)


class ExerciseQuerySet(DateTimeCustomQuerySet):  # noqa
    pass


class Exercise(DateTimeCustom):  # noqa
    finish_date_deadline = models.DateField(
        verbose_name="Дедлайн выполнения"
    )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name="Пользователь"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    activity = models.BooleanField(
        verbose_name="Активное задание",
        default=True
    )
    objects = ExerciseQuerySet().as_manager()

    class Meta:  # noqa
        ordering: List[str] = ["id", ]
        verbose_name_plural: str = "Задания"
        verbose_name: str = "Задание"

    def __str__(self) -> str:  # noqa
        return f'Задание для пользователя {self.user.username}'
