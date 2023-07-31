from django.contrib import admin

from cinema.models import Movie, CinemaHall, Actor, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(CinemaHall)
admin.site.register(Actor)
admin.site.register(Genre)
