from django.contrib import admin

from cinema.models import Actor, CinemaHall, Genre, Movie

admin.site.register([Actor, CinemaHall, Genre, Movie])
