from django.contrib import admin

from cinema.models import Movie, Genre, Actor, CinemaHall

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(CinemaHall)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
