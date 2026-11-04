from django.contrib import admin

from cinema.models import Actor, CinemaHall, Genre, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register([Actor, CinemaHall, Genre])
