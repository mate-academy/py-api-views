from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(to="Genre", related_name="movies")
    actors = models.ManyToManyField(to="Actor", related_name="movies")

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
