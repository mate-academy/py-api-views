from django.contrib import admin

from cinema.models import Movie, Genre, Actor, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = (
        "first_name",
        "last_name",
    )


@admin.register(CinemaHall)
class CinemaHall(admin.ModelAdmin):
    search_fields = ("nama",)
