from django.contrib import admin

from cinema.models import Genre, Actor, CinemaHall, Movie


admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Movie)
