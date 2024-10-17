from django.contrib import admin
from cinema.models import Actor, Genre, CinemaHall, Movie

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(CinemaHall)
admin.site.register(Movie)
