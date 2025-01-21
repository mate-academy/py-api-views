from django.db import models
from cinema_service import settings


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "actor"
        verbose_name_plural = "actors"

    def __str__(self):
        return f"Actor name: ({self.first_name} {self.last_name})"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return (f"Hall name: {self.name}"
                f"(rows: {self.rows}, "
                f" seats: {self.seats_in_row})")


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.title
