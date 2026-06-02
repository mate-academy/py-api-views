from django.contrib import admin

from cinema.models import Actor, CinemaHall, Genre, Movie


admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Genre)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
