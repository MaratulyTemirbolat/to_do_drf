from django.contrib import admin

from to_do_app.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):  # noqa
    list_display: tuple = (
        'finish_date_deadline', 'user',
        'activity',
    )
    readonly_fields: tuple = (
        'date_time_created',
        'date_time_deleted',
        'existance_duration',
    )
