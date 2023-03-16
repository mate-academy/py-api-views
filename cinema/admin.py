from django.contrib import admin

from cinema.models import Movie, Genre, CinemaHall, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)
admin.site.register(CinemaHall)
admin.site.register(Actor)
