from django.contrib import admin

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall,
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(CinemaHall)
