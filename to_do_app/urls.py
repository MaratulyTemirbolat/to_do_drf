from rest_framework.routers import (
    DefaultRouter,
)

from django.urls import (
    path,
    include,
)

from to_do_app.views import (
    AllExercisesApiView,
    # UserExercisesApiView,
    UserViewSet,
    ExerciseViewSet,
)


router: DefaultRouter = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        '',
        AllExercisesApiView.as_view(),
        name="all_exercises"
    ),
    # path(
    #     'user/<int:user_id>/',
    #     UserExercisesApiView.as_view(),
    #     name="user_exercises"
    # ),
]


# ----------------------------------
# User End Point
#

router.register(r'user', UserViewSet)
router.register(r'exercise', ExerciseViewSet)

urlpatterns += [
    path(
        'api/v1/',
        include(router.urls)
    ),
]
