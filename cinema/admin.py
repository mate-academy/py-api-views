from django.contrib import admin

from cinema.models import Movie, CinemaHall, Actor, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.register(CinemaHall)

admin.register(Actor)

admin.register(Genre)
