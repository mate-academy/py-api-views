from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor, related_name="actors_movies")
    genres = models.ManyToManyField(Genre, related_name="genres_movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
