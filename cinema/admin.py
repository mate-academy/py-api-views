from django.contrib import admin

from cinema.models import Movie, Actor, Genre, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Actor)
class AdminActor(admin.ModelAdmin):
    pass


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    pass


@admin.register(CinemaHall)
class AdminCinemaHall(admin.ModelAdmin):
    pass
