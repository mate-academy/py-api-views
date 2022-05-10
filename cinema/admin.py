from django.contrib import admin

from cinema.models import Actor, Genre, CinemaHall, Movie


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
class AdminMovie(admin.ModelAdmin):
    pass
