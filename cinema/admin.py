from django.contrib import admin
from django.contrib.auth.models import Group

from cinema.models import Movie, Genre, Actor, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
