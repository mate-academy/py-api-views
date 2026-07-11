from django.contrib import admin

from cinema.models import Actor
from cinema.models import CinemaHall
from cinema.models import Genre
from cinema.models import Movie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
