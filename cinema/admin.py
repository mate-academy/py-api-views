from django.contrib import admin
from .models import Genre, Actor, CinemaHall, Movie

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(CinemaHall)
admin.site.register(Movie)
