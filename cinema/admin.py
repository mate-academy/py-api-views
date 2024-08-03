from django.contrib import admin

from cinema.models import Movie, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
