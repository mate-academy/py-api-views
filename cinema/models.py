from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(
        Actor, related_name="movies", null=True, blank=True
    )
    genres = models.ManyToManyField(
        Genre, related_name="movies", null=True, blank=True
    )

    def __str__(self):
        return self.title
