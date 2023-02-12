from django.contrib import admin

from cinema.models import Movie, Genre, Actor, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("duration",)
