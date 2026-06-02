from django.contrib import admin

from .models import Movie, Actor, CinemaHall, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Genre)
