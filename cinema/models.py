from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name, self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}(rows:{self.rows}, " \
               f"seats in row: {self.seats_in_row})"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
