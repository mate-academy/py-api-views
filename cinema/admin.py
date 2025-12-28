from django.contrib import admin

from cinema.models import Actor, CinemaHall, Genre, Movie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(CinemaHall)
class CinemaHallAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "display_actors", "display_genres")
    search_fields = ("title", "description")
    list_filter = ("genres", "actors")
    filter_horizontal = ("actors", "genres")

    def display_actors(self, obj):
        return ", ".join([f"{actor.first_name} {actor.last_name}" for actor in
                          obj.actors.all()[:3]])

    display_actors.short_description = "Actors"

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = "Genres"
