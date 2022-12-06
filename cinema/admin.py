from django.contrib import admin

from cinema.models import (
    Movie,
    CinemaHall,
    Genre,
    Actor,
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ...


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    ...


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ...


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    ...
