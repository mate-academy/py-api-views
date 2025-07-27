from django.contrib import admin

from cinema.models import Movie, Actor, CinemaHall, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_actors",
        "display_genres",
        "description",
        "duration",
    )

    def display_actors(self, obj):
        return ", ".join(
            [actor.first_name + " " + actor.last_name for
             actor in obj.actors.all()]
        )

    display_actors.short_description = "Actors"

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = "Genres"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
