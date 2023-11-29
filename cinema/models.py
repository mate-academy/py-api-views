from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField("Actor", related_name="movies")
    genres = models.ManyToManyField("Genre", related_name="movies")
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=83)
    last_name = models.CharField(max_length=83)


class Genre(models.Model):
    name = models.CharField(max_length=83, unique=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=83)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
