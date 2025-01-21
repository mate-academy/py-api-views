from django.contrib import admin

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
)


@admin.register(Actor, CinemaHall, Genre, Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
