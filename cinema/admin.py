from django.contrib import admin
from .models import Actor, Genre, CinemaHall, Movie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rows", "seats_in_row")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration")
    search_fields = ("title",)
    filter_horizontal = ("actors", "genres")
