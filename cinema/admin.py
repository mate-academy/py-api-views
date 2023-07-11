from django.contrib import admin

from cinema.models import Movie, Actor, Genre, CinemaHall

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(CinemaHall)
admin.site.register(Movie)
