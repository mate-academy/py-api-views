from django.contrib import admin

from cinema.models import Movie, Actor, Genre, CinemaHall


@admin.register(Actor)
class Actor(admin.ModelAdmin):
    pass


@admin.register(Genre)
class Genre(admin.ModelAdmin):
    pass


@admin.register(CinemaHall)
class CinemaHall(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
