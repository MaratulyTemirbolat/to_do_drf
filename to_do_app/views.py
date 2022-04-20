from typing import (
    Optional,
)

from rest_framework.views import APIView
from rest_framework.generics import (
    # ListAPIView,
    ListCreateAPIView,
)
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import (
    # IsAdminUser,
    # AllowAny,
    IsAuthenticated,
)
from rest_framework.decorators import action

from django.db.models import QuerySet
from django.contrib.auth.models import User

from to_do_app.models import Exercise
from to_do_app.serializers import (
    ExerciseSerializer,
    UserSerializer,
)


class AllExercisesApiView(ListCreateAPIView):  # noqa
    queryset: QuerySet = Exercise.objects.all()
    serializer_class: ExerciseSerializer = ExerciseSerializer


class UserExercisesApiView(APIView):  # noqa
    def list(self, request: DRF_Request, user_id: int):  # noqa
        exercise: Exercise = Exercise.objects.get(user_id=user_id)
        return DRF_Response(
            {
                'exercises': ExerciseSerializer(exercise).data
            }
        )


class ExerciseViewSet(ViewSet):  # noqa
    queryset: QuerySet = Exercise.objects.get_non_deleted()
    serializer_class: ExerciseSerializer = ExerciseSerializer

    def list(self, request: DRF_Request) -> DRF_Response:  # noqa
        return DRF_Response(
            {
                'exercises': self.serializer_class(
                    self.queryset, many=True
                ).data
            }
        )

    def create(self, request: DRF_Request) -> DRF_Response:  # noqa
        serializer_class = self.serializer_class(
            data=request.data
        )
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return DRF_Response(
            {"exercise": serializer_class.data}
        )


class UserViewSet(ViewSet):  # noqa
    queryset: QuerySet = User.objects.filter(is_active=True)
    permission_classes: tuple = (
        # IsAdminUser,
        # AllowAny,
        IsAuthenticated,
    )
    serializer_class: UserSerializer = UserSerializer

    def list(
        self,
        request: DRF_Request
    ) -> DRF_Response:  # noqa
        return DRF_Response(
            {"message": "Default GET method for User"}
        )

    def create(self, request: DRF_Request) -> DRF_Response:  # noqa
        serializer_class = self.serializer_class(
            data=request.data
        )
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return DRF_Response(
            {"exercise": serializer_class.data}
        )

    def update(
        self,
        request: DRF_Request
    ) -> DRF_Response:  # noqa
        return DRF_Response(
            {"message": "Default PUT method for User"}
        )

    def destroy(
        self,
        request: DRF_Request,
        pk: Optional[int] = None
    ) -> DRF_Response:  # noqa
        return DRF_Response(
            {"message": "Default DELETE method for User"}
        )

    def partial_update(
        self,
        request: DRF_Request,
        pk: Optional[int] = None
    ) -> DRF_Response:  # noqa
        return DRF_Response(
            {"message": "Default PATCH method for User"}
        )

    def retrieve(
        self,
        request: DRF_Request,
        pk: Optional[int] = None
    ) -> DRF_Response:  # noqa
        return DRF_Response(
            {"message": f"Default GET id={pk} method for User"}
        )

    @action(
        methods=['get'],
        detail=True,
        url_path='user_exercise'
    )
    def get_user_exercise(
        self,
        request: DRF_Request,
        pk: Optional[int] = None
    ):  # noqa
        if not pk:
            return DRF_Response(
                {"message": "The pk is not given"}
            )
        try:
            exercise: Exercise = Exercise.objects.get(user_id=pk)
        except Exercise.DoesNotExist:
            return DRF_Response(
                {"message": f"Exercise with {pk} is not found"}
            )
        return DRF_Response(
            {
                'response': ExerciseSerializer(exercise).data
            }
        )
