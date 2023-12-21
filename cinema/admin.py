from django.contrib import admin

from cinema.models import Actor, Genre, CinemaHall, Movie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CinemaHall)
class CinemaHall(admin.ModelAdmin):
    list_display = (
        "name",
        "rows",
        "seats_in_row",
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "duration",
    )
    fieldsets = (
        (None, {"fields": ("title", "description", "duration")}),
        ("Actors and Genres", {"fields": ("actors", "genres")}),
    )
