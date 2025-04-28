from django.contrib import admin

from cinema.models import Movie, Actor, Genre, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "duration"]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ["name", "rows", "seats_in_row"]
