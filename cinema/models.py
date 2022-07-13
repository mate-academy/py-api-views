from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField("Genre")
    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return f"{self.title}"


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class CinemaHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
