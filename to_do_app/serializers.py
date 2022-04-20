from typing import (
    Tuple,
)

from rest_framework.serializers import (
    ModelSerializer,
)

from django.contrib.auth.models import User

from to_do_app.models import Exercise

class ExerciseSerializer(ModelSerializer):  # noqa
    class Meta:  # noqa
        model: Exercise = Exercise
        fields: Tuple[str] = (
            'finish_date_deadline',
            'user',
            'description',
            'activity',
        )


class UserSerializer(ModelSerializer):  # noqa
    class Meta:  # noqa
        model: User = User
        fields: str = '__all__'
