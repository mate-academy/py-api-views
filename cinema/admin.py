from django.contrib import admin

from cinema.models import Movie, Genre, Actor, CinemaHall


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(CinemaHall)
