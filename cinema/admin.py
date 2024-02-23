from django.contrib import admin

from cinema.models import (
    Movie,
    CinemaHall,
    Genre,
    Actor,
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass
