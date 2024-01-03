from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
        blank=True,
        null=True
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
